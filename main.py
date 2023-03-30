from Operation import Operation
import read
import create
import update
import remove

def main():
    data = Operation()
    data.control = read.read_data()
    created_data = {
                "category_id": "1",
                "id": "123456",
                "name": "Intel Core I10",
                "price": 10000000,
                "stock": 10,
                "description": "Best ever"}
    create.create_data(created_data)
    updated_data = created_data = {
                "category_id": "1",
                "id": "123456",
                "name": "Intel Core I10",
                "price": 10000000,
                "stock": 10,
                "description": "Newest model"}
    update.update_data(updated_data)
    remove.remove(updated_data)
    
    

if __name__ == "__main__":
    main()
