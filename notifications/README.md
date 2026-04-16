# Notifications Module - Observer Pattern Implementation

This module demonstrates the **Observer Design Pattern** in the context of a baseball game reporting system. It simulates a baseball game where various observers (reporters) monitor and report on player hit events in different formats.

## Key Features:
- **Observer Pattern**: Decouples the subject (game events) from its observers (reporters)
- **Multiple Report Types**: Log, Table, Graph, and Fan Club reports
- **Event-Driven**: Observers react to hit events as they occur
- **Dynamic Attachment**: Observers can attach/detach from the subject at runtime

## How It Works:
- The `BaseballReporter` (Subject) generates simulated baseball events using `EventMaker`
- Each event represents a player's at-bat result (out, single, double, triple, or home run)
- Attached observers receive notifications and update their reports accordingly
- Different observers produce different output formats:
  - **LogReport**: Sequential list of all hits
  - **TableReport**: Tabular summary by player
  - **GraphReport**: Bar chart visualization of hit types
  - **FanClubReport**: Special bulletin for a specific player's first hit

## UML Diagram

```mermaid
classDiagram
    class Subject {
        -_observers: list
        +attach(observer)
        +detach(observer)
        +notify(player_name)
    }

    class Observer {
        <<abstract>>
        +update(player_name)* string
    }

    class BaseballReporter {
        -_event_maker: EventMaker
        -_current_event: Event
        +current_event
        +report_hits()
    }

    class LogReport {
        -_reporter: BaseballReporter
        -_count: int
        +update(player_name)
    }

    class TableReport {
        -_reporter: BaseballReporter
        -_hit_map: dict
        +update(player_name)
    }

    class GraphReport {
        -_reporter: BaseballReporter
        -_singles: int
        -_doubles: int
        -_triples: int
        -_home_runs: int
        +update(player_name)
    }

    class FanClubReport {
        -_reporter: BaseballReporter
        -_idol: string
        -_what: string
        +print_bulletin()
        +update(player_name)
    }

    class Event {
        -_player_name: string
        -_hit: int
        +player_name
        +hit
    }

    class EventMaker {
        -_name_index: int
        -_outs: int
        -_players_name: tuple
        -_hit_weights: list
        +next_event() Event
    }

    Subject <|-- BaseballReporter
    Observer <|-- LogReport
    Observer <|-- TableReport
    Observer <|-- GraphReport
    Observer <|-- FanClubReport

    BaseballReporter --> EventMaker
    BaseballReporter --> Event
    EventMaker --> Event

    BaseballReporter o-- Observer : notifies
```

## Design Pattern Implementation:
- **Observer Pattern**: The `Subject` class manages a list of observers and notifies them of changes
- **Abstract Base Classes**: `Observer` defines the interface for all concrete observers
- **Composition**: Observers maintain a reference to the subject for accessing event details
- **Loose Coupling**: Subject and observers are independent; new observers can be added without modifying the subject

This design allows easy extension with new report types and promotes maintainable, modular code following the Open/Closed Principle.