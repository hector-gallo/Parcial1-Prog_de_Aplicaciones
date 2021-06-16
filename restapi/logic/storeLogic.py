from core.pyba_logic import PybaLogic

class store_logic(PybaLogic()):
    def __init__(self):
         super().__init__()

    def insertStore(self, store):
        database = self.databaseObj
        sql = (
            "INSERT INTO `sakila`.`store` "
            + f"(`store_id`,`manager_staff_id`,`address_id`,`last_update`) "
            + f"VALUES(0, '{store['manager_staff_id']}', {store['address_id']}, {store['last_update']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
    
    def getStoreById(self, id):
         database = self.databaseObj
         sql = f"SELECT * FROM sakila.store where store_id={id};"
         result = database.executeQuery(sql)
         return result

    def postStore(self):
         database = self.databaseObj
         sql = f"SELECT * FROM sakila.store;"
         result = database.executeQuery(sql)
         return result

    def updateStore(self, id, store):
         database = self.databaseObj
         sql = (
             "UPDATE `sakila`.`store` "
             + f"SET `manager_staff_id` = '{store['manager_staff_id']}', `address_id` = {store['address_id']}, `last_update` = {store['last_update']} "
             + f"WHERE `store_id` = {id};"
         )
         rows = database.executeNonQueryRows(sql)
         return rows

    def deleteStore(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `sakila`.`store` WHERE store_id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows



