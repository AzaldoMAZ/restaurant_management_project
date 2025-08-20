from django.urls import path
from .views import *

urlpatterns = [
    
]

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant Management System</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%); color: #333;">

    <!-- Header -->
    <header style="background: rgba(26, 32, 44, 0.95); padding: 1rem 0; box-shadow: 0 2px 10px rgba(0,0,0,0.3); position: sticky; top: 0; z-index: 100;">
        <nav style="max-width: 1200px; margin: 0 auto; padding: 0 2rem; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 1.8rem; font-weight: bold; color: #f56565; text-decoration: none;">
                🍽️ RestaurantPro
            </div>
            <div style="display: flex; gap: 2rem;">
                <a href="#home" style="color: #e2e8f0; text-decoration: none; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s; font-weight: 500;" onmouseover="this.style.backgroundColor='rgba(245, 101, 101, 0.1)'; this.style.color='#f56565';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#e2e8f0';">Home</a>
                <a href="#products" style="color: #e2e8f0; text-decoration: none; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s; font-weight: 500;" onmouseover="this.style.backgroundColor='rgba(245, 101, 101, 0.1)'; this.style.color='#f56565';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#e2e8f0';">Products</a>
                <a href="#orders" style="color: #e2e8f0; text-decoration: none; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s; font-weight: 500;" onmouseover="this.style.backgroundColor='rgba(245, 101, 101, 0.1)'; this.style.color='#f56565';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#e2e8f0';">Orders</a>
                <a href="#account" style="color: #e2e8f0; text-decoration: none; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s; font-weight: 500;" onmouseover="this.style.backgroundColor='rgba(245, 101, 101, 0.1)'; this.style.color='#f56565';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#e2e8f0';">Account</a>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section style="max-width: 1200px; margin: 0 auto; padding: 4rem 2rem; text-align: center; color: white;">
        <h1 style="font-size: 3.5rem; font-weight: 900; margin-bottom: 1.5rem; background: linear-gradient(45deg, #ffffff, #f7fafc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            Restaurant Management System
        </h1>
        <p style="font-size: 1.25rem; margin-bottom: 2rem; opacity: 0.9; max-width: 700px; margin-left: auto; margin-right: auto; color: #e2e8f0;">
            Streamline your restaurant operations with our comprehensive management solution. Handle orders, manage inventory, track sales, and optimize your restaurant's performance all in one place.
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 2rem;">
            <a href="#" style="background: linear-gradient(45deg, #f56565, #ed8936); color: white; padding: 1rem 2rem; font-size: 1.1rem; font-weight: 600; border: none; border-radius: 10px; text-decoration: none; box-shadow: 0 8px 25px rgba(245, 101, 101, 0.3); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 12px 35px rgba(245, 101, 101, 0.4)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 25px rgba(245, 101, 101, 0.3)';">
                Get Started
            </a>
            <a href="#" style="background: transparent; color: white; padding: 1rem 2rem; font-size: 1.1rem; font-weight: 600; border: 2px solid #f56565; border-radius: 10px; text-decoration: none; transition: all 0.3s;" onmouseover="this.style.backgroundColor='#f56565'; this.style.boxShadow='0 8px 25px rgba(245, 101, 101, 0.3)';" onmouseout="this.style.backgroundColor='transparent'; this.style.boxShadow='none';">
                View Demo
            </a>
        </div>
    </section>

    <!-- Features Section -->
    <section style="background: rgba(255, 255, 255, 0.95); margin: 4rem 2rem; padding: 4rem 2rem; border-radius: 20px; max-width: 1200px; margin-left: auto; margin-right: auto; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);">
        <h2 style="text-align: center; font-size: 2.5rem; font-weight: 800; margin-bottom: 3rem; color: #1a202c;">
            Powerful Features for Your Restaurant
        </h2>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            
            <!-- Feature Card 1 -->
            <div style="background: white; padding: 2.5rem; border-radius: 16px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 25px 50px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 5px 15px rgba(0,0,0,0.08)';">
                <div style="width: 70px; height: 70px; background: linear-gradient(45deg, #f56565, #ed8936); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">
                    📋
                </div>
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: #1a202c;">Order Management</h3>
                <p style="color: #4a5568; line-height: 1.7;">Efficiently track and manage all incoming orders with real-time updates, order status tracking, and seamless kitchen integration.</p>
            </div>

            <!-- Feature Card 2 -->
            <div style="background: white; padding: 2.5rem; border-radius: 16px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 25px 50px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 5px 15px rgba(0,0,0,0.08)';">
                <div style="width: 70px; height: 70px; background: linear-gradient(45deg, #f56565, #ed8936); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">
                    🏠
                </div>
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: #1a202c;">Dashboard Analytics</h3>
                <p style="color: #4a5568; line-height: 1.7;">Get comprehensive insights into your restaurant's performance with detailed analytics, sales reports, and trend analysis.</p>
            </div>

            <!-- Feature Card 3 -->
            <div style="background: white; padding: 2.5rem; border-radius: 16px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 25px 50px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 5px 15px rgba(0,0,0,0.08)';">
                <div style="width: 70px; height: 70px; background: linear-gradient(45deg, #f56565, #ed8936); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">
                    🍽️
                </div>
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: #1a202c;">Product Catalog</h3>
                <p style="color: #4a5568; line-height: 1.7;">Manage your menu items, pricing, ingredients, and availability with an intuitive product management system.</p>
            </div>

            <!-- Feature Card 4 -->
            <div style="background: white; padding: 2.5rem; border-radius: 16px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 25px 50px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 5px 15px rgba(0,0,0,0.08)';">
                <div style="width: 70px; height: 70px; background: linear-gradient(45deg, #f56565, #ed8936); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">
                    👥
                </div>
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: #1a202c;">Account Management</h3>
                <p style="color: #4a5568; line-height: 1.7;">Handle customer accounts, loyalty programs, and staff management with secure user authentication and role-based access.</p>
            </div>

            <!-- Feature Card 5 -->
            <div style="background: white; padding: 2.5rem; border-radius: 16px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 25px 50px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 5px 15px rgba(0,0,0,0.08)';">
                <div style="width: 70px; height: 70px; background: linear-gradient(45deg, #f56565, #ed8936); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">
                    📊
                </div>
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: #1a202c;">Sales Tracking</h3>
                <p style="color: #4a5568; line-height: 1.7;">Monitor daily, weekly, and monthly sales performance with detailed reporting and revenue optimization tools.</p>
            </div>

            <!-- Feature Card 6 -->
            <div style="background: white; padding: 2.5rem; border-radius: 16px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 25px 50px rgba(0,0,0,0.1)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 5px 15px rgba(0,0,0,0.08)';">
                <div style="width: 70px; height: 70px; background: linear-gradient(45deg, #f56565, #ed8936); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 2rem;">
                    ⚙️
                </div>
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: #1a202c;">System Integration</h3>
                <p style="color: #4a5568; line-height: 1.7;">Seamlessly integrate with POS systems, payment gateways, and third-party delivery platforms for complete automation.</p>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section style="background: rgba(245, 101, 101, 0.1); margin: 4rem 2rem; padding: 3rem 2rem; border-radius: 20px; max-width: 1200px; margin-left: auto; margin-right: auto; backdrop-filter: blur(10px);">
        <h2 style="text-align: center; font-size: 2rem; font-weight: 800; margin-bottom: 2rem; color: white;">
            Trusted by Restaurant Owners
        </h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; text-align: center;">
            <div style="color: white;">
                <div style="font-size: 3rem; font-weight: 900; color: #ffffff; margin-bottom: 0.5rem;">500+</div>
                <div style="font-size: 1.1rem; opacity: 0.9;">Restaurants Served</div>
            </div>
            <div style="color: white;">
                <div style="font-size: 3rem; font-weight: 900; color: #ffffff; margin-bottom: 0.5rem;">50K+</div>
                <div style="font-size: 1.1rem; opacity: 0.9;">Orders Processed</div>
            </div>
            <div style="color: white;">
                <div style="font-size: 3rem; font-weight: 900; color: #ffffff; margin-bottom: 0.5rem;">99.9%</div>
                <div style="font-size: 1.1rem; opacity: 0.9;">Uptime</div>
            </div>
            <div style="color: white;">
                <div style="font-size: 3rem; font-weight: 900; color: #ffffff; margin-bottom: 0.5rem;">24/7</div>
                <div style="font-size: 1.1rem; opacity: 0.9;">Support</div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer style="background: rgba(0, 0, 0, 0.2); color: white; text-align: center; padding: 3rem 2rem; margin-top: 4rem;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <div style="display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; flex-wrap: wrap;">
                <a href="#about" style="color: #e2e8f0; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#f56565';" onmouseout="this.style.color='#e2e8f0';">About Us</a>
                <a href="#contact" style="color: #e2e8f0; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#f56565';" onmouseout="this.style.color='#e2e8f0';">Contact</a>
                <a href="#privacy" style="color: #e2e8f0; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#f56565';" onmouseout="this.style.color='#e2e8f0';">Privacy Policy</a>
                <a href="#terms" style="color: #e2e8f0; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#f56565';" onmouseout="this.style.color='#e2e8f0';">Terms of Service</a>
                <a href="#support" style="color: #e2e8f0; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#f56565';" onmouseout="this.style.color='#e2e8f0';">Support</a>
            </div>
            <p style="margin: 0; opacity: 0.8;">&copy; 2025 RestaurantPro Management System. All rights reserved.</p>
        </div>
    </footer>

</body>
</html>