class Task:
    def __init__(self, index, title, description, title_format="capitalize"):
        self.index = index
        self.title = title
        self.description = description
        self.done = False
        self.title_format = title_format

    def _format_title(self):
        if self.title_format == "capitalize":
            return self.title.capitalize()
        elif self.title_format == "title":
            return self.title.title()
        else:
            return self.title

    def mark_done(self):
        self.done = True

    def __str__(self):
        return f"Task {self.index}\nTitle: {self.title}" \
               f"\nDescription: {self.description}" \
               f"\nDone: {self.done}\n{'-' * 30}"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        deleted_task = self.tasks.pop(index)
        self.update_task_indexes()
        return deleted_task

    def update_task_indexes(self):
        for task in self.tasks:
            task.index = self.tasks.index(task) + 1

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def get_task_next_available_index(self):
        return len(self.tasks) + 1

    def get_tasks_length(self):
        return len(self.tasks) + 1


def get_user_choice():
    print("=" * 30)
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Select an option: ")
    print("=" * 30)
    return choice


def add_task_to(task_list):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_task = Task(task_list.get_task_next_available_index(), title, description)
    task_list.add_task(new_task)


def mark_task_done(task_list):
    index = int(input("Enter the index of the task to mark as done: "))
    if 1 <= index <= task_list.get_tasks_length():
        done_task = task_list.tasks[index - 2]
        done_task.mark_done()
        print(f"Task {index} | {done_task.title} - is marked as done.")
    else:
        print("Invalid index.")
        mark_task_done(task_list)


def deleted_task_in(task_list):
    index = int(input("Enter the index of the task to delete: "))
    if 1 <= index <= task_list.get_tasks_length():
        deleted_task = task_list.delete_task(index - 2)
        print(f"Task {index} | {deleted_task.title} - is deleted")
    else:
        print("Invalid index.")


def main():
    task_list = TaskList()

    while True:
        choice = get_user_choice()
        if choice == "1":
            add_task_to(task_list)
        elif choice == "2":
            task_list.list_tasks()
        elif choice == "3":
            mark_task_done(task_list)
        elif choice == "4":
            deleted_task_in(task_list)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
