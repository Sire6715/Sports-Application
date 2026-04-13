# Sports Application

This is a **Sports Application** built in Python that demonstrates the **Strategy design pattern**. The application simulates an athletics department that manages different sports programs with varying categories and types.

## Key Features:
- **Sports Categories**: Varsity (competitive) and Intramural (recreational)
- **Sport Types**: Baseball, Football, and Volleyball
- **Dynamic Strategies**: Each sport uses different strategies for:
  - **Player Recruitment**: Different approaches for varsity vs. intramural players
  - **Venue Reservation**: Stadiums for varsity sports, open fields for intramural

## How It Works:
- The `AthleticsDept` class generates reports for specific sport combinations
- Each sport is represented by a concrete class (e.g., `VarsityBaseball`, `IntramuralVolleyball`)
- Sports use composition with strategy objects for player and venue management
- Running `main.py` generates sample reports showing the recruited players and reserved venues for each sport category/type combination

## UML Diagram

```mermaid
classDiagram
    class AthleticsDept {
        +generate_report(which)
    }
    
    class Sport {
        -_CATEGORY
        -_SPORT_TYPE
        -_player_strategy
        -_venue_strategy
        +CATEGORY
        +SPORT_TYPE
        +player_strategy
        +venue_strategy
        +recruit_players()
        +reserve_venue()
    }
    
    class VarsityBaseball {
        -_CATEGORY = VARSITY
        -_SPORT_TYPE = BASEBALL
    }
    
    class VarsityFootball {
        -_CATEGORY = VARSITY
        -_SPORT_TYPE = FOOTBALL
    }
    
    class IntramuralBaseball {
        -_CATEGORY = INTRAMURAL
        -_SPORT_TYPE = BASEBALL
    }
    
    class IntramuralFootball {
        -_CATEGORY = INTRAMURAL
        -_SPORT_TYPE = FOOTBALL
    }
    
    class IntramuralVolleyball {
        -_CATEGORY = INTRAMURAL
        -_SPORT_TYPE = VOLLEYBALL
    }
    
    class PlayerStrategy {
        <<abstract>>
        +strategy()* string
    }
    
    class VarsityBaseballPlayers {
        +strategy() string
    }
    
    class VarsityFootballPlayers {
        +strategy() string
    }
    
    class IntramuralBaseballPlayers {
        +strategy() string
    }
    
    class IntramuralFootballPlayers {
        +strategy() string
    }
    
    class IntramuralVolleyballPlayers {
        +strategy() string
    }
    
    class VenueStrategy {
        <<abstract>>
        +strategy()* string
    }
    
    class Stadium {
        +strategy() string
    }
    
    class OpenField {
        +strategy() string
    }
    
    class Category {
        <<enumeration>>
        VARSITY
        INTRAMURAL
    }
    
    class SportType {
        <<enumeration>>
        BASEBALL
        FOOTBALL
        VOLLEYBALL
    }
    
    AthleticsDept --> Sport : creates
    Sport --> PlayerStrategy : uses
    Sport --> VenueStrategy : uses
    VarsityBaseball --|> Sport
    VarsityFootball --|> Sport
    IntramuralBaseball --|> Sport
    IntramuralFootball --|> Sport
    IntramuralVolleyball --|> Sport
    
    VarsityBaseballPlayers --|> PlayerStrategy
    VarsityFootballPlayers --|> PlayerStrategy
    IntramuralBaseballPlayers --|> PlayerStrategy
    IntramuralFootballPlayers --|> PlayerStrategy
    IntramuralVolleyballPlayers --|> PlayerStrategy
    
    Stadium --|> VenueStrategy
    OpenField --|> VenueStrategy
    
    Sport --> Category
    Sport --> SportType
```

## Design Pattern Implementation:
- **Strategy Pattern**: The `Sport` class delegates player recruitment and venue reservation to strategy objects, allowing runtime changes in behavior
- **Inheritance**: Concrete sports inherit from the base `Sport` class
- **Composition**: Sports are composed with strategy objects rather than inheriting behavior

This design allows easy extension of new sports or strategies without modifying existing code, following the Open/Closed Principle.
