![Getroman Logo](staticfiles/img/Built_by_dark_badge.png)

## Description
>A feature to help TinyOrganics filter out recipes that do NOT contain any ingredients that a child is allergic to. Mock API's for recipes and allergens provided by TinyOrganics..

### Live Demo
[https://evening-dawn-59182.herokuapp.com/](https://evening-dawn-59182.herokuapp.com/)

### Process
![Process](staticfiles/img/process.png)

### Stories Completed
1. As a new Customer, I should be able to access the home page which contains a form which I will enter my information such as:
   - first name 
   - last name
   - email
   - child's first name
   - child's last name
   - any allergies

2. As a new Customer , I should be given a list of recipes that do NOT contain any ingredients that my child is allergic to. 

### API End Points
- To fetch the list of recipes , make a GET request to 
    - https://60f5adf918254c00176dffc8.mockapi.io/api/v1/recipes/

- To fetch the list of allergens, make a GET request to  
    - https://60f5adf918254c00176dffc8.mockapi.io/api/v1/allergens/
### Tech Stack
##### ```Scaffolding```
- The Django template language 
##### ```Web Framework```
- Python
- Django
##### ```Deployment/Hosting Infrastructure```
- Heroku
### Future Improvements
- Update form page to reload on __init__ vs HTTP page reload
- Include bread crumbs for ease of navigation for user
- Move Frontend consumption from Django templating to React
- Add unit test
- More Future Improvement Updates coming on 8/17. List is currently being curated. 