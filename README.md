<h4 align="center"> 
	🚧 Microservices with FastAPI, an introduction 🚧
</h4>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/rmendes1/web_fastapi_microservices?color=%2304D361">

 <img alt="Repository size" src="https://img.shields.io/github/repo-size/rmendes1/web_fastapi_microservices">
	
  
  <a href="https://github.com/rmendes1/web_fast_api_microservices/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rmendes1/web_fastapi_microservices">
  </a>
  

# **Objective**
_This is a fictional project and only for study purposes_

The purpose of this project is to build a simple microservices app to make 2 endpoints communicate to each other.
The first one is an inventory microservice, where products data will be stored, and the other one will provide a platform
to make an order/purchase of a certain product.

# **Tools**

For this project, FastAPI was used to hold the application backend and the framework is made with React.
The data will be stored in a Redis cloud infrastructure with Redis JSON, which is a tool that retrieves
JSON values to a database, and the events will be sent from one microservice to another using Redis Streams. A Redis Stream is 
a data structure that works as an append-only log and is responsible to record and send events in real time.

A Bootstrap template was used. This template can be found at https://getbootstrap.com/docs/5.2/examples/dashboard/

<p align = "center" > Figure 1 - Architecture used</p>
<h1 align="center"> 
<img src="diagram.png">
</h1>

# **Pages**

## Home Page
Firstly, the user can have access to the page through its index, which contains the list of products with their prices and quantity on stock.
It is possible to delete a product from the list.

<p align = "center" > Figure 2 - Index Page</p>
<h1 align="center">    
    <img src="homepage.png" />
</h1>

## Add a new product (/create)

The user is able to click in the "Add" button in the homepage and submit a new product through the form in figure 3.

<p align = "center" > Figure 3 - Add Product Form</p>
<h1 align="center">    
    <img src="add_form.png" />
</h1>

## Add a new order (/orders)
It is possible to create a new order through the form in figure 4. In order to submit, the user must have the product id.

<p align = "center" > Figure 4 - Login Form</p>
<h1 align="center">
    <img src="order_form.png" />
</h1>

As the user inserts the product id, the price is informed before the user specifies the quantity of products to get.

<p align = "center" > Figure 5 - Filling the Form</p>
<h1 align="center">
    <img src="filling_order_form.png" />
</h1>
