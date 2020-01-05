class Laptops:
    def __init__(self, made, processor, ram, storage):
        self.made_type = made
        self.processor_speed = processor
        self.ram_size = ram
        self.storage_size = storage


class Microprocessor:
    def __init__(self, company, speed, generation):
        self.company_made = company
        self.processor_speed = speed
        self.generation = generation
