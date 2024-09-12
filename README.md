Here’s an updated README for your **Event Approval Tool**  , focusing on department-wise event creation and admin approval, followed by a unified calendar view of all approved events.

---

# Event Approval Tool - Django Application

This Django-based application allows department users to create events that require admin approval. Approved events are displayed in a single calendar view, making it easy to track tasks across departments.

## Features

- **Department-wise event creation**: Users from various departments can create events.
- **Event approval**: Admin users have the ability to approve or reject events.
- **Unified calendar view**: Once approved, all department events are displayed in a consolidated calendar view.
- **Department-based user roles**: Each user belongs to a department, and can only create events for that department.
- **Admin dashboard**: A Django admin interface for event management (approval, rejection).

## Technologies Used

- **Django** - Backend framework.
- **FullCalendar.js** - To display events in a calendar view.
- **SQLite/PostgreSQL/MySQL** - For database storage.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/event-approval-tool.git
cd event-approval-tool
```

### 2. Set Up a Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Database

Configure your database in the `settings.py` file. By default, SQLite is used, but you can switch to PostgreSQL or MySQL if preferred.

Example PostgreSQL configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'event_db',
        'USER': 'your-db-user',
        'PASSWORD': 'your-db-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

After configuring the database, apply the migrations:

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`.

## User Roles and Workflow

1. **Department User**:
   - Logs in to create events for their department.
   - The event details include title, description, date, time, and department.
   - Created events are marked as "pending" until reviewed by an admin.

2. **Admin**:
   - Admin users can view all pending events.
   - Admin can approve or reject events through the Django admin panel.
   - Once approved, the event appears on the unified calendar view visible to all users.

## Event Approval Workflow

1. **Step 1: Event Creation**  
   Department users can create events by filling out an event form that includes details such as title, description, date, and time.

2. **Step 2: Admin Review**  
   Admin logs in to the Django admin interface (`/admin/`) and reviews the submitted events. Admin can either approve or reject the event.

3. **Step 3: Calendar Display**  
   Once approved, the event will appear in the unified calendar view for all users to see. This calendar view is color-coded by department to easily distinguish between department events.

### Calendar View

All approved events are displayed in a unified calendar view, implemented using **FullCalendar.js**. The calendar provides an easy-to-use interface for viewing all department events in a month, week, or day format.

- **Color-coded events**: Each department has a unique color for its events.
- **Event details**: Clicking on an event in the calendar opens a modal with full event details (title, department, description, date, time).

## How to Use the Application

### For Department Users:

1. **Log In**:  
   Navigate to `/login/` and log in using your department credentials.

2. **Create Event**:  
   - Go to the event creation page.
   - Fill out the event form with the required details (title, description, department, date, and time).
   - Submit the form to send the event for admin approval.

3. **View Calendar**:  
   Once your event is approved, you can view it in the calendar along with other department events.

### For Admin Users:

1. **Log In as Admin**:  
   Navigate to `/admin/` and log in using your superuser credentials.

2. **Review Events**:  
   - In the Django admin interface, you can view all submitted events.
   - You can either approve or reject events.

3. **Manage Users and Departments**:  
   The admin can also manage users and assign them to specific departments.

### Calendar Integration

The calendar is integrated into the dashboard, providing an overview of all events across departments:

- **Unified view**: See all department tasks and events in one place.
- **Filter by department**: Optionally filter the calendar view by department or date.
- **Department colors**: Events are color-coded based on the department to provide a clear distinction between them.

## Database Models

### 1. **Event Model**

The event model stores all event-related data.

- `title` (CharField): The name of the event.
- `description` (TextField): A brief description of the event.
- `department` (ForeignKey to Department): The department creating the event.
- `date` (DateField): The date of the event.
- `time` (TimeField): The time of the event.
- `status` (BooleanField): The status of the event (pending/approved/rejected).
- `created_by` (ForeignKey to User): The user who created the event.

### 2. **Department Model**

The department model categorizes users and events.

- `name` (CharField): The name of the department.
- `users` (ManyToManyField): Users assigned to the department.

## Admin Interface

The admin interface (`/admin/`) is used to manage events and users.

- **Approve or Reject Events**: Admins can view all submitted events and approve or reject them.
- **Manage Users and Departments**: Admins can manage the users and their associated departments from the admin dashboard.

## Notifications (Optional)

You can add a notification system where users are notified via email or on-screen notifications when their events are approved or rejected. You can configure this in your `views.py` or by using Django's built-in email handling.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a clear overview of your **Event Approval Tool** project, outlining how department users can create events, how admins can approve or reject them, and how all events are displayed in a unified calendar view.
