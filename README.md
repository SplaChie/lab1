# Zoo Inventory System

## Programming Principles Adherence

### 1. DRY (Don't Repeat Yourself)
The code avoids repetition by creating reusable classes for Animal, Enclosure, Food, Staff, and ZooInventory.

### 2. KISS (Keep It Simple, Stupid)
The implementation is straightforward and easy to understand, with each class serving a single purpose.

### 3. SOLID Principles
- **Single Responsibility Principle**: Each class has a single responsibility (Animal handles animal details, Enclosure handles enclosures, etc.).
- **Open/Closed Principle**: The classes are open for extension but closed for modification.
- **Liskov Substitution Principle**: Objects of subclasses should be replaceable with objects of their base class.
- **Interface Segregation Principle**: Not applicable in this context due to the simple structure.
- **Dependency Inversion Principle**: High-level modules are not dependent on low-level modules.

### 4. YAGNI (You Aren't Gonna Need It)
Only necessary features have been implemented.

### 5. Composition Over Inheritance
Enclosures contain Animals through composition rather than inheritance.

### 6. Program to Interfaces, not Implementations
Interfaces aren't explicitly used, but classes interact through well-defined methods.

### 7. Fail Fast
The code assumes that all provided data is valid and focuses on the happy path, but can be extended to include error checking.

## Code References
- [zoo.py](zoo.py)
- [main.py](main.py)
