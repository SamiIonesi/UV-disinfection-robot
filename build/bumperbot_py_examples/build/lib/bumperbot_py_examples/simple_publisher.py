import rclpy        #importing the ROS2 library for python tha allow us to use all the functionality that is in ROS2
from rclpy.node import Node     #This is the Node class that will allow us to create a ROS2 Node
from std_msgs.msg import String     #importing the string class

class SimplePublisher(Node):        #we are inheritance our class from the Node class
    def __init__(self):     #the constructor
        super().__init__("simple_publisher")

        self.pub_ = self.create_publisher(String, "chatter", 10)     #we are creating a publisher with the specific function from Node class
        #in the parenthesis of the creade_publisher function we specify what type of mesage we will send, in our case a String
        #and also we specify the name of the topic that will gonna send messages and the size of the queue(of the message)

        self.counter_ = 0       #will count the number of topics that we will gonna publish in the chatter topics

        self.frequency_ = 1.0       #the frequency at witch we want to publish the message( in this case is 1s)

        self.get_logger().info("Publishing at %d Hz" % self.frequency_)       #print the message in the console

        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)       #asta va executa in mod continuu o functie la o anumita frecventa

    def timerCallback(self):        #this function will publish a message in the chatter topic each time is executed
        msg = String()
        msg.data = "Hello ROS 2 - counter: %d" % self.counter_      #the message that will be published

        self.pub_.publish(msg)      #this will acually publish the message
        self.counter_ += 1       #the counter will be increased


#Now we will create the main function that will be executed when we will run this script

def main():
    rclpy.init()        #initialize the ros2 interface
    simple_publisher = SimplePublisher()        #the object of our class
    rclpy.spin(simple_publisher)        #will continuously run the object created
    simple_publisher.destroy_node()     #will Ctrl + C we can distroy the node
    rclpy.shutdown()        #we close the ros2 interface

if __name__ == '__main__':
    main()
