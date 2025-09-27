FROM ubuntu:22.04

# Declare build arguments
ARG TEACHER_PASSWORD
ARG STUDENT_PASSWORD

# Install SSH server, sudo, and Python
RUN apt-get update && apt-get install -y openssh-server sudo python3 \
    && mkdir /var/run/sshd

# Create teacher account
RUN useradd -m teacher \
    && echo "teacher:${TEACHER_PASSWORD}" | chpasswd \
    && adduser teacher sudo

# Copy teacher's script
COPY teacher_report.py /home/teacher/teacher_report.py
RUN chmod +x /home/teacher/teacher_report.py \
    && chown teacher:teacher /home/teacher/teacher_report.py

# Create student account with restricted shell
RUN useradd -m -s /bin/rbash student \
    && echo "student:${STUDENT_PASSWORD}" | chpasswd

# Set up student home directory
RUN chown student:student /home/student \
    && chmod 755 /home/student

# Copy the Python script directly into /home/student
COPY runner.py /home/student/runner.py
RUN chmod +x /home/student/runner.py \
    && chown student:student /home/student/runner.py

# Create a bin folder for restricted commands
RUN mkdir /home/student/bin \
    && ln -s /home/student/runner.py /home/student/bin/runner \
    && chown -R student:student /home/student/bin

# Restrict student's PATH to only their bin folder
RUN echo 'export PATH=$HOME/bin' >> /home/student/.bashrc

# Set student's home
RUN usermod -d /home/student student

# Expose SSH port
EXPOSE 22

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]
