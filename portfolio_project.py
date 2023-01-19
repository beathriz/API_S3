import instaloader
from flask import Flask, request, render_template
app = Flask(__name__)

# create an instance of Instaloader
L = instaloader.Instaloader()

# define the username
username = ""

# get profile data
profile = instaloader.Profile.from_username(L.context, username)

# print profile data
print("Profile data: ")
print("Username: ", profile.username)
print("Fullname: ", profile.full_name)
print("Bio: ", profile.biography)
print("Followers: ", profile.followers)
print("Following: ", profile.followees)
print("Is private: ", profile.is_private)

# download profile picture
L.download_profile(profile, "/home/beathrizdev/Desktop")


@app.route("/")
def index():
    return render_template("siteportfolio.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]

    # processar my_input aqui
    result = process_input("username")
    return result

if __name__ == "__main__":
    app.run()
