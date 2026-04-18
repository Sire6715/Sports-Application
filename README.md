# Sports Application

This is a comprehensive **Sports Application** built in Python that demonstrates various software design patterns through different modules. The application simulates a complete sports management system, including athletics departments, player management, ticket sales, equipment provisioning, notifications, and executive access control.

## Overview

The application is organized into several modules, each implementing a specific design pattern:

- **Sports Module**: Factory and Strategy patterns for managing athletics programs
- **Players Module**: Iterator pattern for team player management
- **Provisions Module**: Composite pattern for equipment and uniform organization
- **Tickets Module**: State pattern for ticket vending machine operations
- **Ticket Category Module**: Decorator pattern for ticket enhancements
- **Notifications Module**: Observer pattern for event reporting
- **Executive Module**: Singleton pattern for exclusive access control

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone or download this repository.
3. No additional dependencies are required as the application uses only standard Python libraries.

## Usage

To run the application and see demonstrations of all design patterns:

```bash
python main.py
```

This will execute examples from each module, showing:
- Sports department reports with different categories and venues
- Team player rosters using various data structures
- Equipment cost calculations and hierarchical organization
- Ticket vending machine state transitions
- Enhanced ticket pricing with add-on features
- Baseball game event notifications in multiple formats
- Executive pass singleton behavior

## Project Structure

```
Sports Application/
├── main.py                          # Entry point demonstrating all modules
├── README.md                        # This file
├── sports/                          # Factory & Strategy patterns
│   ├── __init__.py
│   ├── athletics_dept.py            # Abstract/concrete department classes
│   ├── sport.py                     # Base Sport class and enumerations
│   ├── sports.py                    # Concrete sport subclasses
│   ├── provisions_factory.py        # Abstract factory for strategies
│   ├── player_strategy.py           # Player recruitment strategies
│   ├── venue_strategy.py            # Venue reservation strategies
│   └── __pycache__/
├── players/                         # Iterator pattern
│   ├── iterator.py                  # Iterator interface and implementations
│   ├── player.py                    # Player data structures
│   ├── team.py                      # Team classes with different storage
│   ├── report.py                    # Team reporting functionality
│   ├── README.md
│   └── __pycache__/
├── provisions/                      # Composite pattern
│   ├── main.py
│   ├── provision_group.py           # Composite classes
│   ├── provision_item.py            # Component interface
│   ├── equipment.py                 # Equipment items
│   ├── footwear.py                  # Footwear items
│   ├── sunscreen.py                 # Sunscreen item
│   ├── uniform.py                   # Uniform items
│   ├── cost_report.py               # Cost calculation and reporting
│   ├── README.md
│   └── __pycache__/
├── tickets/                         # State pattern
│   ├── main.py
│   ├── state.py                     # State interface
│   ├── states_block.py              # State management
│   ├── ticket_machine.py            # Context class
│   ├── READY.py                     # Ready state
│   ├── SOLD_OUT.py                  # Sold out state
│   ├── TICKET_SOLD.py               # Ticket sold state
│   ├── VALIDATING.py                # Validating state
│   ├── README.md
│   └── __pycache__/
├── ticket_categrory/                # Decorator pattern
│   ├── main.py
│   ├── ticket.py                    # Component interface
│   ├── enhancement.py               # Decorator base
│   ├── README.md
│   └── __pycache__/
├── notifications/                   # Observer pattern
│   ├── subject.py                   # Subject interface
│   ├── observer.py                  # Observer interface
│   ├── baseball_reporter.py         # Concrete subject
│   ├── event.py                     # Event data
│   ├── log_report.py                # Log observer
│   ├── table_report.py              # Table observer
│   ├── graph_report.py              # Graph observer
│   ├── fan_club_report.py           # Fan club observer
│   ├── README.md
│   └── __pycache__/
├── executive/                       # Singleton pattern
│   ├── executivePass.py             # Singleton class
│   ├── main.py
│   ├── README.md
│   └── __pycache__/
└── __pycache__/                     # Python bytecode cache
```

## Design Patterns Implemented

### 1. Factory & Strategy Patterns (Sports Module)
- **Factory Pattern**: Departments create sport objects and provide strategy factories
- **Abstract Factory Pattern**: ProvisionsFactory creates player and venue strategies
- **Strategy Pattern**: Sport objects delegate to strategy objects for behavior

### 2. Iterator Pattern (Players Module)
- Provides uniform access to team players regardless of internal storage (list, generator, dict)
- Supports different iteration mechanisms while maintaining consistent interface

### 3. Composite Pattern (Provisions Module)
- Hierarchical organization of equipment, uniforms, and other provisions
- Uniform treatment of individual items and groups for cost calculation

### 4. State Pattern (Tickets Module)
- Finite state machine for ticket vending with states: READY, VALIDATING, TICKET_SOLD, SOLD_OUT
- Encapsulates state-specific behavior and transitions

### 5. Decorator Pattern (Ticket Category Module)
- Dynamic addition of ticket enhancements (VIP, Party, Coupons) without subclassing
- Transparent cost accumulation and feature stacking

### 6. Observer Pattern (Notifications Module)
- Decoupled event reporting system with multiple observer types (log, table, graph, fan club)
- Automatic notification of subscribers when baseball events occur

### 7. Singleton Pattern (Executive Module)
- Ensures only one executive pass instance exists at any time
- Controlled access to exclusive privileges

## Key Features

- **Modular Design**: Each pattern is implemented in a separate module
- **Educational Value**: Demonstrates practical applications of design patterns
- **Extensible Architecture**: Easy to add new sports, states, decorators, etc.
- **Clean Interfaces**: Consistent APIs across different implementations
- **No External Dependencies**: Pure Python implementation

## Sample Output

The application generates various reports demonstrating each pattern:

```
VARSITY BASEBALL
  players: varsity Baseball players
       venue: stadium

INTRAMURAL VOLLEYBALL
  players: Intramural volleyball players
       venue: open field

Team: Team_1
Player ID: 1, Name: Smith, John
...

Equipment Group - Total Cost: $150
  Ball - $20
  Bat - $50
  ...

Ticket Machine State: READY
Inserting credit card...
Validating card...
Ticket sold! Take your ticket.

Base Ticket: $30
Enhanced Ticket (VIP + Party): $75

Baseball Game Report:
Player: John Smith - Single
...
```

This project serves as both a functional sports management system and a comprehensive reference for implementing design patterns in Python.
