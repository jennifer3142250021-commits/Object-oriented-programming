class user:
    def __init__(self, username, email, age):
        self.username=username
        self.email=email
        self.age=age


    def posted(self,post):
        self.post=post
    def show_post(self):
        print(f"{self.username} posted: {self.post.title}")

    def add_comments(self,comments):
        self.comments=comments
    def show_commnet(self):
        print(f"{self.username}has a comment from {self.comments.author}")

    


    def login(self):
        print(f"the user {self.username} is logged in")



class post:
    def __init__(self,title,content,date):
        self.title=title
        self.content=content
        self.date=date

    def publish(self):
        print(f"the post {self.title} is published")


class comments:
    def __init__(self,author,text,likes):
        self.author=author
        self.text=text
        self.likes=likes

    def like(self):
        print(f"the comment got a like, now has {self.likes+1}likes")

class message:
    def __init__(self, sender, receiver,content):
        self.sender=sender
        self.receiver=receiver
        self.content=content
    def send(self):
        print(f"message form {self.sender.username}to {self.receiver.username} is sent")

#instances
jennifer=user ("Jennifer", "jenni@gmail.com ", 20)
eva = user("Eva", "eva@gmail.com",20)
post= post("my first post", "hello world", "14-09-2026")
comments=comments("Alex", "Nice post!", 5)
message=message("user", "user2", "Hi!")
#cretaing relationships
jennifer.posted(post)
jennifer.add_comments(comments)

#Use the relationship
jennifer.show_post()
jennifer.show_commnet()
message.send()


