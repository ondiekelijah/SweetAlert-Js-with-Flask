<div align="center"><h1>SweetAlert Js with Flask</h1></div>

## Usage :pushpin:
### Points to note:

   - You should be using Bootstrap 5.
   > Find it [here](https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
   - Must include a link to sweetalert2 cdn.
   > Find it [here](https://sweetalert2.github.io/#download)
   - In your flask routes you must be using the message flashing method.
  
### 1. As a template :pushpin:
To use this custom alerts as a template;
- In your templates folder create a file `"sweetalerts.html"` then copy and paste the following lines of code.

```python
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
- Then import the template in your html file as follows.
```
{% include "sweetalerts.html" %}
```
### 2. Inline :pushpin:  
Alternatively,you can just copy and paste the above code snippet inside your html file.

```html
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <!-- Sweet alert Js -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <title>Hello, world!</title>
</head>

<body>
    <div>
                <!-- Begin alerts -->                
                {% with messages = get_flashed_messages(with_categories=true) %}
                {% if messages %}
                {% for category, message in messages %}
                <script>

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
    </div>
    
    {% block content%}
    {% content %}
   ...
    <!-- Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>

</html>
```
### Sample snippets





Success             |  Information
:-------------------------:|:-------------------------:
![Sample](https://github.com/Dev-Elie/SweetAlert-Js-with-Flask/blob/main/static/success.png)  |  ![Sample](https://github.com/Dev-Elie/SweetAlert-Js-with-Flask/blob/main/static/info.png)

Warning             |  Danger
:-------------------------:|:-------------------------:
![Sample](https://github.com/Dev-Elie/SweetAlert-Js-with-Flask/blob/main/static/danger.png)  |  ![Sample](https://github.com/Dev-Elie/SweetAlert-Js-with-Flask/blob/main/static/warning.png)

</br></br>
<div align="center"><h1>Let's connect on Twitter</h1></div>
<p align="center"> <a href="https://twitter.com/dev_elie" target="blank"><img src="https://img.shields.io/twitter/follow/dev_elie?logo=twitter&style=for-the-badge" alt="dev_elie" /></a> </p>
