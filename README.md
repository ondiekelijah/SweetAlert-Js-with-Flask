<div align="center"><h1>SweetAlert Js with Flask</h1></div>

## Usage :pushpin:
### 1. As a template :pushpin:
To use this custom alerts as a template;
- In your templates folder create a file `"sweetalerts.html"` then copy and paste the following lines of code.

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
- Then import the template in your html file as follows.
```
{% include "sweetalerts.html" %}
```
### 2. Inline :pushpin:  
ALternatively,you can just copy and paste the above code snippet inside your html file.
          

</br></br></br>
<div align="center"><h1>Let's connect on Twitter</h1></div>
<p align="center"> <a href="https://twitter.com/dev_elie" target="blank"><img src="https://img.shields.io/twitter/follow/dev_elie?logo=twitter&style=for-the-badge" alt="dev_elie" /></a> </p>
