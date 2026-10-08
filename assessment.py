# Build a command-line Campus Resource Management System in Python.
"""
Learn2Earn lends equipment to fellows. 
Build a working Python program that stores resource inventory, 
issues items, accepts returns, searches inventory and produces accurate reports.
"""
# REQUIREMENT
"""
1. Resource inventory (10): Every resource has unique ID, name, category, total units and available units.
Add and list resources; reject duplicate IDs.
2. Borrowing (15): Check fellow ID and resource ID; quantity must be a positive integer and no greater than stock.
Log every successful borrowing and reduce availability. Rejected attempts must not mutate state.
"""

resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

def list_resources():
    for res in resources:
        print(f"Id: {res['id']} | Name: {res['name']} | Category: {res['category']} | Total: {res['total']} | Avaliable: {res['available']}")
list_resources()



def resource_inventory(new_resources_id, name, category, total):
    for res in resources:
        # validating resource entry
        if res["id"] == new_resources["id"]:
            print("id already exist")
            return False
    new_resources= {
    "id" : new_resources_id,
    "name": name,
    "category": category,
    "total": total,
    "avalible": total
    }
     # adding new resource entry 
    resources.append(new_resources)
    print("successfuly add an item")
    return True
def borrow_item(fellows_id, quty, resource_id):
    # validate fellows id
    if fellows_id not in fellows:
        print(f"Rejection: Fellow Id {fellows_id} is not a registered fellow")
        return
    # validate quantity 
    if quty < 0:
        print(f"Rejection: Quantity must be a positive integer")
        return
    new_res = None
    for r in resources:
        if r['id'] == resource_id:
           new_res = resource_id
           break
    if not new_res:
        print(f"Rejection: Resources Id {resource_id} does not exists ")
        return
    if quty > new_res['available']:
        print(f"Rejection: Qu")
