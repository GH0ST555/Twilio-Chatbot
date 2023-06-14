#all the routes for my website go here

#import relevant modules
import os
from app import app
from flask import render_template, flash,redirect,request, make_response,json,url_for,jsonify
from flask_login import LoginManager,login_required,logout_user,login_user,current_user
from flask_mail import Mail, Message
from .forms import NewRec




#it is a sample view to test a sample JSON File with flask. as i am not very familiar with JSON i am trying an example

@app.route('/', methods=['GET','POST'])
def load_all():
    #loads the first and last name from the json file
    #embeds the data into a template
    with open("app/static/adress.json", "r+") as f:
        data=json.load(f)
        f.close()
    if data is None:
        return render_template('404.html'), 404
    return render_template('viewall.html', data=data)


#route that helps in creation of a new record
@app.route('/create_user', methods=['GET','POST'])
def create_record():
    form = NewRec()
    with open("app/static/adress.json", "r+") as f:
        data=json.load(f)
        f.close()
    if form.validate_on_submit():
        for row in data:
            nid=row['id']
        newid = int(nid) + 1
        nid = str(newid)
        #store all the data from the form into a dictionary
        dictionary = {
        "id": nid,
        "first_name":form.fname.data,
        "last_name": form.lname.data,
        "phone":str(form.pno.data),
        "email":form.email.data
        }
        # Serializing json
        #open the file to load data
        with open("app/static/adress.json", "r+") as f:
            data1=json.load(f)
            f.close()
        data1.append(dictionary)
        # Writing to our flat file, we append the new data from our form.
        with open("app/static/adress.json", "w") as outfile:
            json.dump(data1, outfile, indent=4,  separators=(',',': '))
            outfile.close()
            return redirect('/')
            
    return render_template('create.html', form=form)

@app.route('/delete/<id>', methods=['GET','POST'])
#deeltes a row using its id
#redirects to homepage after deletion
def delete_record(id):
    p_row=None
    with open("app/static/adress.json", "r+") as f:
        data1=json.load(f)
        f.close()
    for row in data1:
        if row['id'] == id:
            p_row = row
    if p_row is None:
        return render_template('404.html'), 404
    # Iterate through the objects in the JSON and pop (remove)                      
    # the obj once we find it.                                                      
    for i in range(len(data1)):
        if data1[i]["id"] == id:
            data1.pop(i)
            break
    with open("app/static/adress.json", "w") as outfile:
        json.dump(data1, outfile, indent=4,  separators=(',',': '))    
        outfile.close()        
    return redirect('/')   

    
@app.route('/edit/<id>', methods=['GET','POST'])
def edit_record(id):
    #to edit the record we do it a bit creativrly
    #we delete the record and re-enter the updated data
    #id's also get sorted in ascending oreder to ensure no errors ocour when data is added
    p_row=None
    with open("app/static/adress.json", "r+") as f:
        datas=json.load(f)
        f.close()
    
    for row in datas:
        if row['id'] == id:
            p_row = row
    if p_row is None:
        return render_template('404.html'), 404

    form1 = NewRec()
    if form1.validate_on_submit():
        with open("app/static/adress.json", "r+") as f:
            data1=json.load(f)
        # Iterate through the objects in the JSON and pop (remove)                      
        # the obj once we find it.                                                      
        for i in range(len(data1)):
            if data1[i]["id"] == id:
                data1.pop(i)
                break
        dictionary = {
        "id": id,
        "first_name":form1.fname.data,
        "last_name": form1.lname.data,
        "phone":str(form1.pno.data),
        "email":form1.email.data
        }
        data1.append(dictionary)
        data1.sort(key=lambda x: x["id"])
        with open("app/static/adress.json", "w") as outfile:
            json.dump(data1, outfile, indent=4,  separators=(',',': '))
            outfile.close()
            return redirect('/')
        
    return render_template('edit.html',form=form1,data=p_row)


@app.route('/view', methods=['GET','POST'])
def load_record():
    #gets the id from the request
    #get the row information from the id
    #start get the json record and embedd it into template
    id = request.args.get('id')  
    p_row=None
    with open("app/static/adress.json", "r+") as f:
        datas=json.load(f)
        f.close()
    for row in datas:
        if row['id'] == id:
            p_row = row
    if p_row is None:
        return render_template('404.html'), 404
    return render_template('userpage.html', data=p_row)

   