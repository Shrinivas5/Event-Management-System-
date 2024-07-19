import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

# Function to display analytics dashboard
def show_analytics_dashboard():
    # Load event data
    data = pd.read_csv('event_data.csv')

    # Create a new window for the analytics dashboard
    dashboard = tk.Toplevel()
    dashboard.title("Event Analytics Dashboard")

    # Create a frame for the charts
    chart_frame = ttk.Frame(dashboard)
    chart_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Function to plot attendance rates
    def plot_attendance():
        fig, ax = plt.subplots()
        data.plot(kind='bar', x='event_name', y='attendance', ax=ax)
        ax.set_title('Event Attendance Rates')
        ax.set_xlabel('Event')
        ax.set_ylabel('Attendance')

        # Display the plot
        plt.show()

    # Function to plot feedback scores
    def plot_feedback():
        fig, ax = plt.subplots()
        data.plot(kind='bar', x='event_name', y='feedback_score', ax=ax, color='orange')
        ax.set_title('Event Feedback Scores')
        ax.set_xlabel('Event')
        ax.set_ylabel('Feedback Score')

        # Display the plot
        plt.show()

    # Add buttons to plot the charts
    btn_attendance = ttk.Button(chart_frame, text="Plot Attendance Rates", command=plot_attendance)
    btn_attendance.pack(pady=10)

    btn_feedback = ttk.Button(chart_frame, text="Plot Feedback Scores", command=plot_feedback)
    btn_feedback.pack(pady=10)

    # Run the dashboard
    dashboard.mainloop()

# Main application function
def main_app():
    root = tk.Tk()
    root.title("Event Management System")

    # Button to open the analytics dashboard
    btn_analytics = ttk.Button(root, text="Show Analytics Dashboard", command=show_analytics_dashboard)
    btn_analytics.pack(pady=20)

    root.mainloop()

# Run the main application
if __name__ == "__main__":
    main_app()
