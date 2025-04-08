from time import sleep

class Process:
  def __init__(self, name, remaining_time):
    self.name = name
    self.remaining_time = remaining_time
    self.next = None

  def __str__(self):
    return self.name
  

class RoundRobinScheduler:
  def __init__(self, time_quantum):
    self.head = None
    self.time_quantum = time_quantum

  def add_process(self, name, remaining_time):
    new_process = Process(name, remaining_time) 

    if not self.head:
      self.head = new_process
      new_process.next = self.head
  
      return new_process
    
    current_process = self.head

    while current_process.next != self.head:
      current_process = current_process.next

    current_process.next = new_process
    new_process.next = self.head

    return new_process

  def run(self):
    print("Starting Round Robin Scheduling...")

    current_process = self.head
    prev_process = None

    while current_process.remaining_time > 0:
      remaining_time = current_process.remaining_time - self.time_quantum

      if remaining_time > 0:
        print(f"Process {current_process.name} ran for {self.time_quantum} units. Remaining: {remaining_time}")
      else:
        print(f"Process {current_process.name} completed in {current_process.remaining_time} units.")

        if prev_process:
          prev_process.next = current_process.next

      current_process.remaining_time = remaining_time

      prev_process = current_process if remaining_time > 0 else prev_process
      current_process = current_process.next

      sleep(1)


scheduler = RoundRobinScheduler(time_quantum=4)
scheduler.add_process("A", 2)
scheduler.add_process("B", 6)
scheduler.add_process("C", 8)
scheduler.add_process("D", 16)

scheduler.run()