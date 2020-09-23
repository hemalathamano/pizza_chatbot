from flask import jsonify


def generateResponse(data, msg):
    response_data = {}
    data_list = []
    try:
        for i in data:
            temp = {}
            temp["order_id"] = i[0]
            temp["name"] = i[1]
            temp["pizza_name"] = i[2]
            temp["pizza_type"] = i[3]
            temp["pizza_size"] = i[4]
            temp["phone_no"] = i[5]
            temp["status"] = i[6]
            data_list.append(temp)
            response_data["data"] = data_list

        response_data["msg"] = msg
        print(f"Respone data : {response_data}")
        return jsonify(response_data)
    except IndexError as e:
        print(e)
        return str(e)

