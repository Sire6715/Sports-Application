# Tickets Module - State Design Pattern Implementation

This module demonstrates the **State Design Pattern** in the context of a ticket vending machine for sports events. The machine manages ticket sales through different states, handling credit card validation, ticket dispensing, and sold-out conditions.

## Key Features:
- **State Pattern**: Encapsulates state-specific behavior and transitions
- **Dynamic State Changes**: Machine behavior changes based on current state
- **Finite State Machine**: Well-defined states and transitions
- **Context Management**: TicketMachine maintains current state and shared data

## How It Works:
- The `TicketMachine` (Context) starts in the `READY` state
- User interactions (insert card, check validity, take ticket, remove card) trigger state transitions
- Each state defines behavior for all possible actions:
  - **READY**: Accepts card insertion, waits for validation
  - **VALIDATING**: Simulates card validation (80% success rate)
  - **TICKET_SOLD**: Allows ticket dispensing, then returns to READY or SOLD_OUT
  - **SOLD_OUT**: Rejects all operations when tickets are exhausted
- State transitions occur based on user actions and machine conditions

## UML Diagram

```mermaid
stateDiagram-v2
    [*] --> READY
    READY --> VALIDATING : insert_credit_card()
    VALIDATING --> TICKET_SOLD : check_validity() [valid]
    VALIDATING --> READY : check_validity() [invalid]
    TICKET_SOLD --> READY : take_ticket() [tickets > 0]
    TICKET_SOLD --> SOLD_OUT : take_ticket() [tickets == 0]
    READY --> SOLD_OUT : initialize() [count == 0]
    SOLD_OUT --> SOLD_OUT : any action
    READY --> READY : remove_credit_card()
    TICKET_SOLD --> TICKET_SOLD : insert_credit_card() / check_validity()
    VALIDATING --> VALIDATING : insert_credit_card()
```

```mermaid
classDiagram
    class TicketMachine {
        -_states_block: StatesBlock
        -_state: State
        -_count: int
        -_card_inserted: bool
        -_card_validity: Validity
        +insert_credit_card()
        +check_validity()
        +take_ticket()
        +remove_credit_card()
        +run()
    }

    class State {
        <<abstract>>
        -_name: string
        -_machine: TicketMachine
        +name
        +states
        +count
        +card_inserted
        +card_validity
        +insert_credit_card()*
        +check_validity()*
        +take_ticket()*
        +remove_credit_card()*
    }

    class StatesBlock {
        +READY: READY
        +VALIDATING: VALIDATING
        +TICKET_SOLD: TICKET_SOLD
        +SOLD_OUT: SOLD_OUT
        +initialize(machine) READY
    }

    class READY {
        +insert_credit_card()
        +check_validity()
        +take_ticket()
        +remove_credit_card()
    }

    class VALIDATING {
        +insert_credit_card()
        +check_validity()
        +take_ticket()
        +remove_credit_card()
    }

    class TICKET_SOLD {
        +insert_credit_card()
        +check_validity()
        +take_ticket()
        +remove_credit_card()
    }

    class SOLD_OUT {
        +insert_credit_card()
        +check_validity()
        +take_ticket()
        +remove_credit_card()
    }

    class Validity {
        <<enumeration>>
        YES
        NO
        UNKNOWN
    }

    TicketMachine --> State : current state
    TicketMachine --> StatesBlock
    StatesBlock --> READY
    StatesBlock --> VALIDATING
    StatesBlock --> TICKET_SOLD
    StatesBlock --> SOLD_OUT
    State <|-- READY
    State <|-- VALIDATING
    State <|-- TICKET_SOLD
    State <|-- SOLD_OUT
    State --> TicketMachine : machine
    State --> Validity
```

## Design Pattern Implementation:
- **State Pattern**: Each state is a separate class implementing the State interface
- **Context**: TicketMachine delegates actions to the current state object
- **State Transitions**: States return the next state, which the context adopts
- **Shared State**: States access machine properties through the context
- **Singleton States**: State objects are created once and reused

This design allows easy addition of new states and behaviors without modifying existing code, following the Open/Closed Principle. The state machine ensures the ticket vending process is robust and handles edge cases like sold-out conditions and invalid cards.