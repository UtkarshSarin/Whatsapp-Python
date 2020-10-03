from twilio.rest import Client
import json
import uuid

account_sid = 'AC5238d3ca1f938161673c843ca85f8894'
auth_token = '000e64817b080de1e6326e0da0f18b5e'
client = Client(account_sid, auth_token)

def number(string_length=10):

    random = str(uuid.uuid4())

    random = random.upper()

    random = random.replace("-","")

    return random[0:string_length]

y = input(f'Choose a movie from the following list: \n1: Avengers \n2: Revengers\n')

if y != '1' or y != '2':
    print


# some JSON:
x =  '{ "1":"Avengers", "2":"Revengers"}'

# parse x:
z = json.loads(x)



a = input(f'Choose a movie timing: \n1: 12:00 pm \n2: 3:00 pm \n3: 6:00 pm \n4: 9:00 pm\n')

b = '{"1":"12:00 pm", "2":"3:00 pm", "3":"6:00 pm", "4":"9:00 pm"}'

c = json.loads(b)

print(f'How many people are going? (Max Limit upto 10 tickets)')

d = int(input("Adults:"))
e = int(input("Kids (below the age of 15):"))

total = d * 150 + e * 75

tax = total * 0.18

total_amt = int(total) + int(tax)


#print(z[y])
#print(c[a])

print(f"Your booking details are as follows \nUTN: {number(6)} \nMovie Name: {z[y]} \nTime: {c[a]} \nAdults: {int(d)} \nKids: {int(e)} \nTicket Total: {int(total)} \nTax: {int(tax)} \nTotal Amount: {int(total_amt)} \nThe Ticket is being sent to you via Whatsapp on your Registered Mobile Number")
myticket = (f"*Welcome to Sarin's Cinema* \n\n\nYour booking details that will be sent to you are as follows \nUTN: {number(6)} \nMovie Name: {z[y]} \nTime: {c[a]} \nAdults: {int(d)} \nKids: {int(e)} \nTicket Total: {int(total)} \nTax: {int(tax)} \nTotal Amount: {int(total_amt)}")

message = client.messages.create(
                              body=myticket,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+918384005257'
                          )



