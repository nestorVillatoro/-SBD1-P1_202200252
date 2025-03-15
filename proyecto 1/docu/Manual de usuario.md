# Manual de usuario

## Descripción de la API

API_BD1_P1


POST
Crear Usuario
http://127.0.0.1:5000/api/users


Body
raw (json)
json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123",
  "phone": "12345678"
}
POST
Iniciar Sesión
http://127.0.0.1:5000/api/users/login


Body
raw (json)
json
{
  "username": "jdoe",
  "password": "secret123"
}
GET
Obtener Perfil de Usuario
http://127.0.0.1:5000/users/1


PUT
Actualizar Usuario
http://127.0.0.1:5000/users/1


Body
raw (json)
json
{
  "phone": "87654321",
  "email": "john@example.com"
}
DELETE
Eliminar Usuario
http://127.0.0.1:5000/users/1


GET
Listar Productos
http://127.0.0.1:5000/products


POST
Crear Producto
http://127.0.0.1:5000/products


Body
raw (json)
json
{
  "name": "Laptop X",
  "description": "Laptop de alto rendimiento",
  "price": 750.00,
  "stock": 10,
  "category": "Electrónicos"
}
PUT
Actualizar Producto
http://127.0.0.1:5000/products


Body
raw (json)
json
{
  "price": 700.00,
  "stock": 15
}
DELETE
Eliminar Producto
http://127.0.0.1:5000/products


GET
Listar Órdenes
http://127.0.0.1:5000/orders


PUT
Actualizar Estado de una Orden
http://127.0.0.1:5000/orders/101


Body
raw (json)
json
{
  "status": "shipped"
}
POST
Registrar un Pago
http://127.0.0.1:500/payments


Body
raw (json)
json
{
  "order_id": 101,
  "amount": 1800.00,
  "method": "credit_card"
}
GET
Listar Pagos
http://127.0.0.1:500/payments

## Endpoints Utilizados
```
{
	"info": {
		"_postman_id": "bb29ae34-6d2f-445d-9893-03f0ae13e75d",
		"name": "API_BD1_P1",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "30659605"
	},
	"item": [
		{
			"name": "Crear Usuario",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"username\": \"testuser\",\r\n  \"email\": \"test@example.com\",\r\n  \"password\": \"password123\",\r\n  \"phone\": \"12345678\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/users",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"users"
					]
				}
			},
			"response": []
		},
		{
			"name": "Iniciar Sesión",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"username\": \"jdoe\",\r\n  \"password\": \"secret123\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/users/login",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"users",
						"login"
					]
				}
			},
			"response": []
		},
		{
			"name": "Obtener Perfil de Usuario",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/users/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"users",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "Actualizar Usuario",
			"request": {
				"method": "PUT",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"phone\": \"87654321\",\r\n  \"email\": \"john@example.com\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/users/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"users",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "Eliminar Usuario",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/users/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"users",
						"1"
					]
				}
			},
			"response": []
		},
		{
			"name": "Listar Productos",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/products",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"products"
					]
				}
			},
			"response": []
		},
		{
			"name": "Crear Producto",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"name\": \"Laptop X\",\r\n  \"description\": \"Laptop de alto rendimiento\",\r\n  \"price\": 750.00,\r\n  \"stock\": 10,\r\n  \"category\": \"Electrónicos\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/products",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"products"
					]
				}
			},
			"response": []
		},
		{
			"name": "Actualizar Producto",
			"request": {
				"method": "PUT",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"price\": 700.00,\r\n  \"stock\": 15\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/products",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"products"
					]
				}
			},
			"response": []
		},
		{
			"name": "Eliminar Producto",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/products",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"products"
					]
				}
			},
			"response": []
		},
		{
			"name": "Listar Órdenes",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/orders",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"orders"
					]
				}
			},
			"response": []
		},
		{
			"name": "Actualizar Estado de una Orden",
			"request": {
				"method": "PUT",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"status\": \"shipped\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/orders/101",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"orders",
						"101"
					]
				}
			},
			"response": []
		},
		{
			"name": "Registrar un Pago",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"order_id\": 101,\r\n  \"amount\": 1800.00,\r\n  \"method\": \"credit_card\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:500/payments",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "500",
					"path": [
						"payments"
					]
				}
			},
			"response": []
		},
		{
			"name": "Listar Pagos",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:500/payments",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "500",
					"path": [
						"payments"
					]
				}
			},
			"response": []
		}
	]
}
```