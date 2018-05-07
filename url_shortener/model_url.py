"""Flask model for testing demo."""


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):
    """Employee."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    state = db.Column(db.String(2), nullable=False, default='CA')
    dept_code = db.Column(db.String(5), db.ForeignKey('department.dept_code'))

    dept = db.relationship('Department')

    def __repr__(self):
        return "<Employee id=%d name=%s>" % (self.id, self.name)

    def to_dict(self):
        """Turn a employee into a dictionary.

        Useful for JSONification.

        Handles employees without departments:

            >>> leonard = Employee(name='Leonard', state='CA')
            >>> expected =  {'state': 'CA',
            ...              'id': None,
            ...              'dept_code': None,
            ...              'name': 'Leonard'}
            >>> leonard.to_dict() == expected
            True

        If the employee has a department, shows that:

            >>> legal = Department(dept_code='legal', dept='Legal', phone='555-1212')
            >>> leonard = Employee(name='Leonard', state='CA', dept=legal)
            >>> expected =  {'dept': {'dept': 'Legal', 'phone': '555-1212'},
            ...              'state': 'CA',
            ...              'id': None,
            ...              'dept_code': None,
            ...              'name': 'Leonard'}
            >>> leonard.to_dict() == expected
            True
        """

        info = {'id': self.id,
                'name': self.name,
                'state': self.state,
                'dept_code': self.dept_code,
                }
        if self.dept is not None:
            info['dept'] = {
                'dept': self.dept.dept,
                'phone': self.dept.phone,
            }
        return info