# Проектирование базы данных PitGo

## Part 1. Выбор сценария

Для данной работы выбран собственный бизнес-сценарий — **PitGo: система управления клиентами, автомобилями и заказами автосервиса**.

Репозиторий проекта: [PitGO на GitHub](https://github.com/DeathRustZzZ/PitGO.git).

PitGo представляет собой приложение для взаимодействия клиентов и автосервисов. Система предназначена для хранения информации о клиентах и их автомобилях, учёта истории владения транспортными средствами.

---

## Part 2. Проектирование базы данных и документация

### 2.1. Основные сущности

Идентификация сущностей и атрибутов:

1. **Customer (`customers`)** — клиент системы.
2. **Customer Contact Book (`customer_contact_books`)** — контактная информация клиента.
3. **Vehicle (`vehicles`)** — автомобиль.
4. **Vehicle Ownership (`vehicle_ownerships`)** — история владения автомобилями.

### 2.2. Проектирование таблиц

#### 2.2.1. Таблица `customers`

**Description:** таблица `customers` хранит основную информацию о клиенте и состояние его учётной записи. Контактные данные намеренно не находятся непосредственно в этой таблице, а вынесены в `customer_contact_books`.

**Attributes:**

| Атрибут      | Тип данных        | Ключ | Ограничения   | Описание                             |
| ------------ | ----------------- | :--: | ------------- | ------------------------------------ |
| `id`         | `UUID`            |  PK  | `PRIMARY KEY` | Уникальный идентификатор клиента     |
| `status`     | `customer_status` |  —   | `NOT NULL`    | Статус клиента                       |
| `version`    | `BIGINT`          |  —   | `NOT NULL`    | Версия записи для optimistic locking |
| `created_at` | `TIMESTAMPTZ`     |  —   | `NOT NULL`    | Дата и время создания                |
| `updated_at` | `TIMESTAMPTZ`     |  —   | `NOT NULL`    | Дата и время последнего изменения    |

Для `status` используется перечисление `customer_status`.

Предполагаемые значения:

- `draft`;
- `active`.

Поле `version` используется для механизма **optimistic locking** и позволяет обнаруживать конкурентные изменения одной записи.

**Constraints:**

```sql
PRIMARY KEY (id)
CHECK (version >= 0)
```

#### 2.2.2. Таблица `customer_contact_books`

**Description:** таблица содержит контактные данные клиента и информацию о подтверждении телефонного номера. Контактная информация отделена от основной сущности клиента, поскольку имеет собственный жизненный цикл: телефон может отсутствовать, быть добавлен, ожидать подтверждения или быть подтверждён.

**Attributes:**

| Атрибут               | Тип данных            |  Ключ  | Ограничения                               | Описание                 |
| --------------------- | --------------------- | :----: | ----------------------------------------- | ------------------------ |
| `customer_id`         | `UUID`                | PK, FK | `PRIMARY KEY`, `REFERENCES customers(id)` | Клиент                   |
| `phone_number`        | `VARCHAR(20)`         |   —    | —                                         | Номер телефона           |
| `verification_status` | `verification_status` |   —    | `NOT NULL`                                | Статус подтверждения     |
| `verified_at`         | `TIMESTAMPTZ`         |   —    | —                                         | Время подтверждения      |
| `aggregate_version`   | `BIGINT`              |   —    | —                                         | Версия контактных данных |

`customer_id` одновременно является первичным и внешним ключом. Благодаря этому одному клиенту не может соответствовать более одной записи `customer_contact_books`.

**Constraints:**

```sql
PRIMARY KEY (customer_id)

FOREIGN KEY (customer_id)
    REFERENCES customers(id)
```

#### 2.2.3. Таблица `vehicles`

**Description:** таблица `vehicles` представляет автомобиль как самостоятельную сущность. Связь автомобиля с клиентом намеренно не хранится непосредственно в `vehicles`. Для этого используется отдельная таблица `vehicle_ownerships`, благодаря чему можно хранить историю владельцев.

**Attributes:**

| Атрибут      | Тип данных       | Ключ | Ограничения   | Описание                 |
| ------------ | ---------------- | :--: | ------------- | ------------------------ |
| `id`         | `UUID`           |  PK  | `PRIMARY KEY` | Идентификатор автомобиля |
| `status`     | `vehicle_status` |  —   | `NOT NULL`    | Статус автомобиля        |
| `version`    | `BIGINT`         |  —   | `NOT NULL`    | Версия записи            |
| `created_at` | `TIMESTAMPTZ`    |  —   | `NOT NULL`    | Время создания           |
| `updated_at` | `TIMESTAMPTZ`    |  —   | `NOT NULL`    | Время изменения          |

Предполагаемые значения `vehicle_status`:

- `draft`;
- `active`.

**Constraints:**

```sql
PRIMARY KEY (id)
CHECK (version >= 0)
```

#### 2.2.4. Таблица `vehicle_ownerships`

**Description:** `vehicle_ownerships` хранит информацию о владении автомобилями клиентами.

Таблица позволяет определить текущего владельца автомобиля, а также сохранить информацию о предыдущих владельцах. Через неё реализуется логическая связь **многие-ко-многим** между `customers` и `vehicles`:

- один клиент может владеть несколькими автомобилями;
- один автомобиль в разные периоды времени может принадлежать разным клиентам.

**Attributes:**

| Атрибут             | Тип данных         | Ключ | Ограничения                            | Описание               |
| ------------------- | ------------------ | :--: | -------------------------------------- | ---------------------- |
| `id`                | `UUID`             |  PK  | `PRIMARY KEY`                          | Идентификатор владения |
| `vehicle_id`        | `UUID`             |  FK  | `NOT NULL`, `REFERENCES vehicles(id)`  | Автомобиль             |
| `owner_customer_id` | `UUID`             |  FK  | `NOT NULL`, `REFERENCES customers(id)` | Владелец               |
| `ownership_type`    | `ownership_type`   |  —   | `NOT NULL`                             | Тип владения           |
| `status`            | `ownership_status` |  —   | `NOT NULL`                             | Статус владения        |
| `started_at`        | `TIMESTAMPTZ`      |  —   | `NOT NULL`                             | Начало владения        |
| `ended_at`          | `TIMESTAMPTZ`      |  —   | —                                      | Окончание владения     |
| `version`           | `BIGINT`           |  —   | `NOT NULL`                             | Версия записи          |
| `created_at`        | `TIMESTAMPTZ`      |  —   | `NOT NULL`                             | Время создания         |
| `updated_at`        | `TIMESTAMPTZ`      |  —   | `NOT NULL`                             | Время изменения        |

Возможные типы владения (`ownership_type`):

- `private`;
- `company`;
- `leasing`;
- `fleet`;
- `unknown`.

Возможные статусы (`status`):

- `pending_verification`;
- `active`;
- `ended`.

**Constraints:**

```sql
PRIMARY KEY (id)

FOREIGN KEY (vehicle_id)
    REFERENCES vehicles(id)

FOREIGN KEY (owner_customer_id)
    REFERENCES customers(id)

CHECK (ended_at IS NULL OR ended_at >= started_at)

CHECK (version >= 0)
```

Для сохранения целостности данных и предотвращения ситуации, когда один автомобиль может иметь несколько активных владельцев одновременно, создаётся уникальный индекс:

```sql
CREATE UNIQUE INDEX uq_vehicle_open_ownership
ON vehicle_ownerships (vehicle_id)
WHERE status IN ('pending_verification', 'active');
```

### 2.3. Связи между таблицами

#### Customers — Customer Contact Books

**Тип связи:** один-к-одному (`1 : 1`).

Один клиент может иметь одну запись контактной информации. Каждая запись контактной информации относится к одному клиенту. Поскольку `customer_id` одновременно является PK, создать две контактные книги одному клиенту невозможно.

#### Customers — Vehicle Ownerships

**Тип связи:** один-ко-многим (`1 : N`).

Один клиент может иметь множество записей владения автомобилями.

#### Vehicles — Vehicle Ownerships

**Тип связи:** один-ко-многим (`1 : N`).

Один автомобиль может иметь несколько записей владения в разные периоды времени.

#### Customers — Vehicles

**Тип связи:** многие-ко-многим (`M : N`).

Один клиент может владеть несколькими автомобилями. Один автомобиль может принадлежать разным клиентам в разные периоды времени.
