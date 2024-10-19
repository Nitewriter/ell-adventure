# Text Adventure Game System Design Document Using ell

- [ell Documentation](https://docs.ell.so/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Textual Documentation](https://textual.textualize.io/)

## 1. Introduction

This document details the design of a text adventure game using the ell LMP framework. The system uses a planner-executor architecture where a central planner (the Game Master) orchestrates the game’s flow, delegating tasks to modular tools and dynamic agents. The aim is to create an engaging, replayable text adventure experience that can be personalized using player-provided novels or custom narrative inputs.

## 2. Game Architecture Overview

- **Planner (Game Master)**

  - Acts as the central decision-making unit.
  - Interprets player inputs and dynamically manages game progression.
  - Executes tools and spins up agents by drafting a system prompt, assigning necessary tools, and giving a task to perform. The planner then starts the agent and waits for task completion, adapting the story and game environment in real-time.
  - Maintains a consistent game state through ChromaDB for persistence.

- **Tools and Agents**
  - The planner utilizes a collection of specialized tools for managing various game mechanics (e.g., inventory, NPC interactions).
  - Agents are dynamically created to perform temporary roles (e.g., NPC conversations, quest deliveries).

## 3. Game Systems and Tools

### 3.1 Core Systems (Highest Priority)

- **Inventory System Tool**

  - Manages player inventory (add, remove, inspect items).
  - Interfaces with other tools like the combat and equipment systems.
  - State persistence through ChromaDB.

- **Dialogue System for NPC Interactions**

  - Manages and stores NPC interactions, ensuring consistent behavior across sessions.
  - Dynamically generates dialogue options and maintains NPC histories using ChromaDB.

- **World State and Location Tracker**

  - Manages environment details, tracking player movements and state changes. For example, tracking when the player enters a town from the forest, then moves to the inn from the town square. Additionally, the system can adapt to changes like a town being ransacked by orcs and becoming abandoned, or recognizing the player as a hero if they successfully defend it.
  - Integrates with the save system for consistent player experience across sessions.

- **Combat Resolution Tool**
  - Handles combat mechanics including turn-based actions and health calculations.
  - Collaborates with the inventory system for weapon and item effects.
  - Logs outcomes and player stats in ChromaDB.

### 3.2 Secondary Systems (Medium Priority)

- **Currency and Economy Tool**

  - Manages in-game currency and trading mechanics.
  - Supports dynamic pricing and NPC bartering systems.

- **Companion/Pet Management System**

  - Tracks and manages companions, pets, or mercenary hirelings.
  - Coordinates abilities and behavior, updating states persistently in ChromaDB.

- **Event and Quest Tracking System**
  - Logs player quests and game events, providing updates and tracking progress.
  - Can trigger world events and coordinate with other systems for consistency.

### 3.3 Additional Systems (Lower Priority/Future Expansion)

- **Map and Exploration System**

  - Provides navigation support, generating visual/textual maps based on exploration.

- **Skill and Character Progression Tool**

  - Tracks player skills and abilities, managing level progression and upgrades.

- **Weather and Time System**
  - Controls dynamic environmental elements, influencing gameplay (e.g., night/day cycles).

## 4. Game State and Persistence

- **Save System**

  - The game uses ChromaDB for state persistence, storing all critical game elements like NPC states, world conditions, and player progress.
  - Snapshot functionality ensures the player can save manually, at designated points, or automatically whenever there is a change in game state (e.g., inventory, equipment, friendships, or enemies made).

- **Game World Restoration**
  - When a player returns, the latest snapshot is loaded, ensuring continuity.

## 5. Narrative Customization

### 5.1 Novel Integration

- If a player provides a novel:
  - The Content Parser Tool analyzes the text to extract relevant themes, settings, and character archetypes. An LLM can be used for this feature extraction to leverage its ability to understand complex narrative structures. Additionally, consider exploring other methods like rule-based systems or hybrid approaches for feature extraction to broaden the tool's versatility.
  - The planner uses this structured information to adapt game mechanics, NPCs, and environments to align with the novel’s tone and style.

### 5.2 Custom Game Description

- Players can provide a few paragraphs describing their ideal game setup:
  - The Story Seed Generator Tool transforms this input into structured game elements such as setting, primary conflict, and character backstory.
  - The planner builds the initial game world based on these elements, storing them in ChromaDB for consistency.

## 6. Dynamic Narrative Adaptation

- **Dynamic Narrative Weaving Tool**
  - Allows the planner to adjust story arcs based on player input and past actions.
  - For novel-based games, it ensures thematic coherence, using extracted elements to generate plot points and quests.
  - For custom descriptions, it evolves the narrative based on the player’s chosen game path.

## 7. Development and Prioritization Strategy

1. **Initial Development**: Focus on building the core systems (Inventory, Dialogue, World State, and Combat) and integrating them with the save system for a functional MVP.
2. **Secondary Systems**: Implement Currency, Companion Management, and Quest Tracking to deepen gameplay mechanics.
3. **Expansion and Polishing**: Develop additional systems like Mapping, Skill Progression, and Environmental Dynamics to enhance replayability and immersion.

## 8. Tools and Frameworks

- **ell LMP Framework**: Core system for defining and managing the planner, tools, and agents.
- **ChromaDB**: Utilized for persistent data storage and retrieval, ensuring consistency across game sessions.
- **ell Studio**: For version control, visualization, and monitoring of the LMPs, allowing iterative development and debugging.

## 9. Final Notes

- The system’s modularity ensures flexibility in adding new mechanics and story elements.
- Emphasizing player customization (novel or description) allows for personalized, replayable experiences, making each adventure unique.

This design document lays the foundation for your text adventure game using ell. It ensures we have a clear plan for developing the core mechanics first and expanding features incrementally. What do you think? Any sections you’d like to adjust or expand upon further?
