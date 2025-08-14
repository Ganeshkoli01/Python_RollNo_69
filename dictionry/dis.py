# dis={
          
#     "age":12,
#     "name":"ganesh koli",
#      "dis1":{
#     "college name":"dypcet",
#                    "age":12,
#                    "name":"ganesh koli",
#                }    
#                    "college name":"dypcet"  
# }
# #dis["name"]="gk"
# #dis["roll no"]=91
# print(dis.items())
# #print(type(dis))
# #print((dis))
# print(len(dis))


#Q3
marks={}

x=int(input("enter the physice mark:"))
marks.update({"phy":x})

x=int(input("enter the chemistry mark:"))
marks.update({"chemistry":x})

x=int(input("enter the maths mark:"))
marks.update({"maths":x})

print(marks)