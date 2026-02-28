# Client-Server-Development
CS-340-10521-M01 Client/Server Development 2026 C-1 (Jan - Mar)
# Grazioso Salvare Animal Shelter Dashboard

## Project Overview
This project is a full-stack web application dashboard developed for Grazioso Salvare, a company that identifies and trains search-and-rescue dogs. The dashboard provides an interactive interface to query and visualize data from the Austin Animal Center, helping identify dogs suitable for different types of rescue training (Water Rescue, Mountain/Wilderness Rescue, and Disaster/Individual Tracking).

**Author:** Kelly Reinersman  
**Course:** CS-340 Client/Server Development  
**Institution:** Southern New Hampshire University

## Motivation
Grazioso Salvare needed a way to efficiently identify and categorize dogs from animal shelter data based on specific breed, age, and sex requirements for different rescue training programs. This dashboard streamlines their workflow by providing:
- Interactive filtering by rescue type
- Visual data representation through charts
- Geolocation mapping of available dogs
- Real-time database queries

## Project Structure
```
project/
├── CRUD_Python_Module.py          # Database access layer (Model)
├── ProjectTwoDashboard.ipynb      # Dashboard application (View/Controller)
├── README.md                       # This file
└── screenshots/                    # Application screenshots
```

## Installation

### Prerequisites
- Python 3.11.2 or higher
- MongoDB 7.0.21 or higher
- Jupyter Lab
- Required Python packages (see below)

### Required Python Packages
```bash
pip install pymongo
pip install pandas
pip install plotly
pip install dash
pip install dash-leaflet
pip install jupyter-dash
```

### Database Setup
1. Import the Austin Animal Center data:
```bash
mongoimport --type=csv --headerline --db aac --collection animals --drop /datasets/aac_shelter_outcomes.csv
```

2. Create database user:
```bash
mongosh
use aac
db.createUser({
  user: "aacuser",
  pwd: "your_password",
  roles: [{ role: "readWrite", db: "aac" }]
})
```

3. Create indexes for query optimization:
```bash
db.animals.createIndex({ breed: 1 })
db.animals.createIndex({ breed: 1, outcome_type: 1 })
```

## Usage

### Running the Dashboard
1. Open Jupyter Lab in your Codio environment
2. Navigate to `ProjectTwoDashboard.ipynb`
3. Update the username and password in the notebook if needed:
```python
username = "aacuser"
password = "your_password"
```
4. Run all cells in the notebook
5. Access the dashboard at the provided URL (typically `http://localhost:8050`)

### Using the Dashboard Features

**Filter Options:**
- **Water Rescue:** Displays dogs suitable for water rescue training
  - Breeds: Labrador Retriever Mix, Chesapeake Bay Retriever, Newfoundland
  - Sex: Intact Female
  - Age: 26-156 weeks
  
- **Mountain/Wilderness Rescue:** Shows dogs for mountain/wilderness training
  - Breeds: German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, Rottweiler
  - Sex: Intact Male
  - Age: 26-156 weeks
  
- **Disaster/Individual Tracking:** Lists dogs for disaster rescue
  - Breeds: Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, Rottweiler
  - Sex: Intact Male
  - Age: 20-300 weeks
  
- **Reset:** Returns to unfiltered view showing all dogs

**Interactive Features:**
- Click filter buttons to query the database
- Sort and filter data table columns
- Select rows to view dog location on map
- View breed distribution in pie chart

## Code Examples

### CRUD Module Usage
```python
from CRUD_Python_Module import AnimalShelter

# Initialize connection
shelter = AnimalShelter(username="aacuser", password="your_password")

# Create - Insert a new document
new_dog = {
    "animal_id": "A123456",
    "name": "Max",
    "animal_type": "Dog",
    "breed": "Labrador Retriever Mix",
    "age_upon_outcome_in_weeks": 52
}
shelter.create(new_dog)

# Read - Query documents
water_rescue_dogs = shelter.read({
    "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever"]},
    "sex_upon_outcome": "Intact Female",
    "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
})

# Update - Modify documents
shelter.update(
    {"animal_id": "A123456"},
    {"outcome_type": "Adoption"}
)

# Delete - Remove documents
shelter.delete({"animal_id": "A123456"})
```

## Tools and Technologies

### Database
- **MongoDB 7.0.21:** NoSQL database for storing animal shelter data
  - Chosen for flexible schema and ability to handle nested documents (offices array)
  - Supports powerful aggregation pipelines for complex queries
  - Excellent Python integration via PyMongo

### Backend
- **Python 3.11.2:** Primary programming language
  - Object-oriented CRUD module for database operations
  - Extensive library support for data manipulation
  
- **PyMongo 2.5.3:** MongoDB driver for Python
  - Provides Pythonic interface to MongoDB
  - Supports all MongoDB operations

### Frontend
- **Dash/Plotly:** Interactive dashboard framework
  - Creates responsive web applications
  - Built-in components for data visualization
  - Callback system for interactivity
  
- **Dash Leaflet:** Geolocation mapping
  - Interactive maps with markers and popups
  - Real-time updates based on user selection

### Development Environment
- **Codio:** Cloud-based development platform
- **Jupyter Lab:** Interactive notebook environment for development and testing

## Project Architecture (MVC Pattern)

### Model (CRUD_Python_Module.py)
- Handles all database operations
- Encapsulates MongoDB connection logic
- Provides clean interface for CRUD operations
- Methods: `create()`, `read()`, `update()`, `delete()`

### View (Dashboard Layout)
- HTML/CSS layout using Dash components
- Data table for displaying query results
- Pie chart for breed distribution
- Geolocation map for selected animals
- Filter buttons for rescue types

### Controller (Callback Functions)
- `update_dashboard()`: Filters data based on rescue type selection
- `update_graphs()`: Updates pie chart when data changes
- `update_map()`: Updates geolocation marker when row selected
- `update_styles()`: Handles visual feedback for user interactions

## Roadmap / Future Enhancements

### Planned Features
- [ ] Add more rescue type categories
- [ ] Implement user authentication system
- [ ] Add ability to mark dogs as "selected for training"
- [ ] Export filtered results to CSV/PDF
- [ ] Add email notifications for new matching dogs
- [ ] Create mobile-responsive design
- [ ] Add historical tracking of rescue dog placements
- [ ] Implement advanced search with multiple criteria
- [ ] Add dashboard for shelter administrators

### Known Issues
- Map requires valid latitude/longitude coordinates (some records may be missing)
- Large datasets (10,000+ records) may cause initial load delay
- Breed names must match exactly (case-sensitive)

## Reflection Questions

### 1. Maintainable, Readable, and Adaptable Programs
**How do you write programs that are maintainable, readable, and adaptable?**

I approached the CRUD Python module with several key principles:
- **Separation of Concerns:** The CRUD module is completely separate from the dashboard, making it reusable across projects
- **Clear Documentation:** Each method includes docstrings explaining parameters, return values, and functionality
- **Error Handling:** Try-except blocks catch and handle database errors gracefully
- **Consistent Naming:** Methods follow CRUD naming convention (create, read, update, delete)
- **Configuration Management:** Database credentials can be passed as parameters for flexibility

**Advantages of this approach:**
- The CRUD module was used seamlessly in both Project One and Project Two
- Easy to test each method independently
- Can be reused for any MongoDB database project by changing connection parameters
- Clear interface makes it easy for other developers to understand and use

**Future use:**
- This modular approach can be applied to any database-backed application
- The pattern can be extended to include additional operations (aggregate, bulk operations)
- Similar modules can be created for other databases (SQL, Firebase, etc.)

### 2. Problem-Solving as a Computer Scientist
**How do you approach a problem as a computer scientist?**

My approach to the Grazioso Salvare project differed from previous assignments in several ways:

**Previous Assignments:**
- Focused on implementing specific technical requirements
- Clear specifications with defined inputs and outputs
- Individual work without considering client needs

**Grazioso Salvare Project:**
- Started with client needs analysis - understanding their business requirements
- Translated business requirements into technical specifications
- Designed database queries based on domain expertise (rescue dog characteristics)
- Created user-friendly interface considering non-technical users
- Iterative development with multiple rounds of refinement

**Techniques and Strategies:**
1. **Requirements Analysis:** Carefully read specifications to understand all constraints
2. **Incremental Development:** Built features one at a time (filters → table → charts → map)
3. **Testing at Each Stage:** Verified each component worked before moving to next
4. **Documentation:** Maintained clear code comments and README throughout

**Future Database Projects:**
- Start with entity-relationship modeling before writing code
- Create user stories to understand client workflows
- Build modular components that can be tested independently
- Use version control for tracking changes
- Consider scalability and performance from the beginning

### 3. Computer Scientists' Role and Impact
**What do computer scientists do, and why does it matter?**

Computer scientists solve problems by creating automated systems that improve efficiency, accuracy, and accessibility. In the Grazioso Salvare project specifically:

**What We Do:**
- Transform manual, time-consuming processes into automated workflows
- Create tools that make complex data accessible to non-technical users
- Build systems that scale from small to large datasets
- Connect different technologies (databases, web frameworks, visualization tools)

**Why It Matters to Grazioso Salvare:**
- **Time Savings:** Searching through thousands of shelter records manually would take hours; the dashboard does it in seconds
- **Better Decisions:** Visual representation of data helps identify patterns and make informed choices
- **Consistency:** Automated queries ensure consistent application of training criteria
- **Scalability:** As shelter data grows, the system continues to work efficiently
- **Mission Impact:** Faster dog identification means more lives saved in rescue operations

**Broader Impact:**
This type of work demonstrates how technology can support humanitarian missions. By making data actionable, we enable organizations like Grazioso Salvare to focus on their core mission - saving lives - rather than getting bogged down in data management.

## Contact
**Kelly Reinersman**  
Southern New Hampshire University  
CS-340 Client/Server Development

## License
This project was developed as part of academic coursework at Southern New Hampshire University.

## Acknowledgments
- Austin Animal Center for providing the dataset
- Grazioso Salvare for the project specifications
- SNHU CS-340 course materials and instructors
