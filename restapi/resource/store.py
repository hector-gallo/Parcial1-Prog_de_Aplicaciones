from flask_restful import Resource, reqparse
from logic.storeLogic import store_logic

class store(Resource):
     def __init__(self):
           self.store_put_args = self.createParser()

     def createParser(self):
           args = reqparse.RequestParser()
           args.add_argument("store_id", type=int, help="id of the store")
           args.add_argument("manager_staff_id", type=int, help="id of the manager")
           args.add_argument("address_id", type=int, help="id of the adress")
           args.add_argument("last_update", type=int, help="time of the last update")
           return args

     def get(self, id):
           logic = store_logic()
           result = logic.getStoreById (id)
           if len(result) == 0:
             return {}
           return result[0], 200

     def post(self):
           logic = store_logic()
           result = logic.postStore()
           return 200

     def put(self, id):
           store = self.store_put_args.parse_args()
           logic = store_logic()
           rows = logic.insertStore(store)
           return {"rowsAffected": rows}, 200
    
     def patch(self, id):
           store = self.store_put_args.parse_args()
           logic = store_logic()
           rows = logic.updateStore(id, store)
           return {"rowsAffected": rows}, 200

     def delete(self, id):
           logic = store_logic()
           rows = logic.deleteStore(id)
           return {"rowsAffected": rows}, 200

