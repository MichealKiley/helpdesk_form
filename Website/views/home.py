from flask import Blueprint, redirect, render_template, request, flash

home_route = Blueprint("home_route", __name__)


# preliminary questions
@home_route.route("/", methods=['GET','POST'])
def home():
    global issue_type
    if request.method == "POST":
        issue_type = request.form.get("issue_type")

        if issue_type == "printer":
            return redirect("/requester_name", code=302)
        
        if issue_type == "computer":
            return redirect("/user-type", code=302)
        
        if issue_type == "other":
            return redirect("/user-type", code=302)

    return render_template("index.html")


# preliminary questions
@home_route.route("/user-type", methods=['GET','POST'])
def user():
    global user_type
    if request.method == "POST":
        user_type = request.form.get("user_type")

        return redirect("/requester_name", code=302)

    return render_template("user_choice.html")


# preliminary questions
@home_route.route("/requester_name", methods=['GET','POST'])
def name():
    global user_name
    if request.method == "POST":
        user_name = request.form.get("name")

        try:

            # checking if printer or other was selected
            if issue_type == "printer":
                return redirect("/printer-issues", code=302)
            if issue_type == "other":
                return redirect("/other-issues", code=302)

            # redirecting user to computer pages
            if user_type == "yes" and issue_type == "computer":
                return redirect("/pc-another-user", code=302)
            if user_type == "no" and issue_type == "computer":
                return redirect("/pc-current-user", code=302)
            
        except:
            return redirect("/", code=302)

    return render_template("requester_name.html")





# current user computer issues
@home_route.route("/pc-current-user", methods=['GET','POST'])
def current():
    if request.method == "POST":

        #assigning variables
        client_ip = str(request.environ['REMOTE_ADDR'])
        department = request.form.get("dept")
        frequency = request.form.get("frequency")
        subject = request.form.get("subject")
        description = request.form.get("desc")

        print(user_name)
        print(department)
        print(frequency)
        print(subject)
        print(description)
        print(client_ip)
        
        return redirect("/thanks", code=302)

    return render_template("Current_user_form.html")

# another user computer issues
@home_route.route("/pc-another-user", methods=['GET','POST'])
def different():
    if request.method == "POST":

        #assigning variables
        client_ip = str(request.environ['REMOTE_ADDR'])
        pc_name = request.form.get("pc_name")
        department = request.form.get("dept")
        frequency = request.form.get("frequency")
        subject = request.form.get("subject")
        description = request.form.get("desc")

        print(user_name)
        print(pc_name)
        print(department)
        print(frequency)
        print(subject)
        print(description)
        print(client_ip)
        
        return redirect("/thanks", code=302)

    return render_template("different_user_form.html")
    
# printer issues
@home_route.route("/printer-issues", methods=['GET','POST'])
def printer():
    if request.method == "POST":
        
        department = request.form.get("dept")
        printer_name = request.form.get("printer_name")
        printer_issue = request.form.get("printer_issue")
        other_description = request.form.get("desc")

        print(user_name)
        print(department)
        print(printer_name)
        print(printer_issue)
        print(other_description)

        return redirect("/thanks", code=302)

    return render_template("printer_issues.html")


# other issues
@home_route.route("/other-issues", methods=['GET','POST'])
def other():
    if request.method == "POST":
        
        return redirect("/thanks", code=302)

    return render_template("other_issues.html")



@home_route.route("/thanks", methods=['GET','POST'])
def thanks():
    if request.method == "POST":
        
        return redirect("/", code=302)

    return render_template("Thanks_page.html")