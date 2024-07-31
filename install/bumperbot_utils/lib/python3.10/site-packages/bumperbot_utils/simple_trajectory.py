import rclpy
from rclpy.node import Node


class SimpleTrajectory(Node):
    def __init__(self):
        super().__init__("simple_trajectory")