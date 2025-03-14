class Todo:
    def __init__(self,code_id:int,title:str,description:str):
        self.code_id:int = code_id
        self.title:str  = title
        self.description: str = description
        self.completed: bool= False
        self.tags: list[str] = []

    def mark_completed (self):
        self.completed=True

    def add_tag(self,tag:str):

        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos = {}
    def add_todo(self,title:str,description:str):
        code_id=len(self.todos)+1
        todo= Todo(code_id,title,description)
        self.todos.update(todo)
        return code_id
