from operations import make_account_id

class Customer:
    """A class for customers"""
    priority_level = False

    def __init__(self, name, service_request=None, is_prior=False):
        self.name = name
        self.service = service_request
        self.priority = is_prior

    def set_priority(self, is_prior):
        """Sets priority level of the customer"""
        self.priority = is_prior

    def issue_ticket(self):
        if self.priority:
            self.ticket_ID = 'P'
        else:
            self.ticket_ID = 'C'
        self.ticket_ID = self.ticket_ID + make_account_id('C-')
        return self.ticket_ID

    def __repr__(self):
        firstname,surname,other_name = 0,1,2
        return f'''
            Customer Name: {self.name[surname]}, {self.name[firstname]} {self.name[other_name]}
            Type of Service: {self.service}
            Ticket ID: {self.ticket_ID}
        '''
