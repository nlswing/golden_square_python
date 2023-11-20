class TodoList:
    def __init__(self):
        self._todos = []
        
        

    def add(self, todo):
        self._todos.append(todo)
        
       
      
    def incomplete(self):
        return self._todos
        
        

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        completed_todos =[]
        for task in self._todos:
            if task.task_list['complete'] == True:
                completed_todos.append(task)
        return completed_todos
    
        
      

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self._todos:
            task.task_list['complete'] = True
                
            
            