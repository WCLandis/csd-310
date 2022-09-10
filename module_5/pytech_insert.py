from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.yhxm0bp.mongodb.net/?retryWrites=true&w=majority";
client= MongoClient(url)
db=client.pytech

Bill = {
    "student_id": "1007",
    "first_name": "Bill",
    "last_name": "Gates"
}

Steve = {
    "student_id": "1008",
    "first_name": "Steve",
    "last_name": "Jobs"
}

William = {
    "student_id": "1009",
    "first_name": "William",
    "last_name": "Landis"
}

students= db.students

print("\n  -- INSERT STATEMENTS --")
Bill_student_id = students.insert_one(Bill).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(Bill_student_id))

Steve_student_id = students.insert_one(Steve).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(Steve_student_id))

William_student_id = students.insert_one(William).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(William_student_id))

input("\n\n  End of program, press any key to exit... ")
