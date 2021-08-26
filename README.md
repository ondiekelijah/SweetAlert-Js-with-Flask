<div align="center"><h1>SweetAlert Js with Flask</h1></div>

## Usage :pushpin:
### 1. As a template :pushpin:
To use this custom alerts as a template;
In your templates folder create a file "sweetalerts.html" then copy and paste the following lines of code.

```html
   <!-- Begin alerts -->                
   {% with messages = get_flashed_messages(with_categories=true) %}
   {% if messages %}
   {% for category, message in messages %}
   
   Swal.fire({

          title:"{{ category.title() }}!",
          // success , error , warning ,info

          text: "{{ message }}",
          // Custom message flashed from your flask routes

          icon: "{{ category }}" == "danger" ? "error" : "{{ category }}"
          // success , error , warning ,info

   })

   </script>
   {% endfor %}
   {% endif %}
   {% endwith %}

   <!-- End alerts -->
```
### 2. Inline :pushpin:  
          
```
git clone https://github.com/Dev-Elie/Exploring-Flask_SQLAlchemy-Queries.git
cd Exploring-Flask_SQLAlchemy-Queries
py -3 -m venv venv
```
          
**macOS/Linux**
          
```
git clone https://github.com/Dev-Elie/Exploring-Flask_SQLAlchemy-Queries.git
cd Exploring-Flask_SQLAlchemy-Queries
python3 -m venv venv
```

### 2 .Activate the environment :pushpin:
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install Flask-SQLAlchemy :pushpin:

Applies for windows/macOS/Linux

``` pip install Flask-SQLAlchemy ```
  
### 4. Execute python script to create a simple database :pushpin:

**For linux and macOS**

```python create.py```

Open a python shell on your machine and proceed with the exploring queries in the article 
</br></br></br>
<div align="center"><h1>Happy Learning :+1: </h1></div>
<p align="center"> <a href="https://twitter.com/dev_elie" target="blank"><img src="https://img.shields.io/twitter/follow/dev_elie?logo=twitter&style=for-the-badge" alt="dev_elie" /></a> </p>
