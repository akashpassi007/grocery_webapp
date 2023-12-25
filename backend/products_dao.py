from sql_connection import get_sql_connection

# fetch the data from database.
def get_all_products(connection):
    cursor = connection.cursor()

    # query = ("SELECT * FROM grocerystore.products")
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, "
             "uom.uom_name from products inner join uom on uom.uom_id = products.uom_id")

    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    return response

# Insert the data in the database.

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = ("insert into products (name, uom_id, price_per_unit) values (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit() # save the data.

    return cursor.lastrowid

# Delete product from the database.

def delete_product(connection, product_id):
    cursor = connection.cursor()

    query = ("Delete FROM products where product_id = "+ str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # if connection:
    #     print(get_all_products(connection))
    # else:
    #     print("Failed to establish a database connection.")

#Insert data in the database command.
    # print(insert_new_product(connection, {
    #     'product_name': 'Panner',
    #     'uom_id': '2',
    #     'price_per_unit': '120'
    # }))

# Delete data in the databse.
    print(delete_product(connection,10))

