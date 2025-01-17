import random

positions_data = []

for vessel_index in range(5):
    vessel_name = f"Tàu {chr(65 + vessel_index)}"
    latitude = random.uniform(18.9, 19.5)
    longitude = random.uniform(106.0, 107.0)

    for position_index in range(20):
        positions_data.append(
            {
                "vessel_name": vessel_name,
                "latitude": round(latitude, 6),
                "longitude": round(longitude, 6),
            }
        )

        latitude += random.uniform(-0.02, 0.02)
        longitude += random.uniform(-0.02, 0.02)

crew_data = [
    {
        "name": "John Doe",
        "role": "Thuyền trưởng",
        "phone": "1234567890",
        "address": "123 Đường Biển",
        "unit": "A1",
        "vessel_name": "Tàu A",
    },
    {
        "name": "Jane Smith",
        "role": "Kỹ sư",
        "phone": "9876543210",
        "address": "456 Làng Cảng",
        "unit": "B2",
        "vessel_name": "Tàu B",
    },
    {
        "name": "Sam Wilson",
        "role": "Thủy thủ",
        "phone": "5647382910",
        "address": "789 Đại lộ Bến Tàu",
        "unit": "C3",
        "vessel_name": "Tàu C",
    },
    {
        "name": "Anna Johnson",
        "role": "Đầu bếp",
        "phone": "1928374650",
        "address": "321 Đường Ven Nước",
        "unit": "D4",
        "vessel_name": "Tàu A",
    },
    {
        "name": "Lucas Brown",
        "role": "Thợ máy",
        "phone": "2938475610",
        "address": "654 Cảng Bắc",
        "unit": "E5",
        "vessel_name": "Tàu D",
    },
    {
        "name": "Emily Davis",
        "role": "Nhân viên y tế",
        "phone": "3748291056",
        "address": "987 Khu vực Trung Tâm",
        "unit": "F6",
        "vessel_name": "Tàu E",
    },
]

vessels_data = [
    {
        "name": "Tàu A",
        "registration_number": "NA1234567",
        "address": "Cảng A",
        "status": "active",
        "description": "Mô tả A",
        "speed": 20.5,
        "captain_name": "Nguyễn Văn A",
        "captain_phone": "1234567890",
    },
    {
        "name": "Tàu B",
        "registration_number": "NA2345678",
        "address": "Cảng B",
        "status": "inactive",
        "description": "Mô tả B",
        "speed": 30.0,
        "captain_name": "Trần Thị B",
        "captain_phone": "9876543210",
    },
    {
        "name": "Tàu C",
        "registration_number": "NA3456789",
        "address": "Cảng C",
        "status": "sunk",
        "description": "Mô tả C",
        "speed": 15.0,
        "captain_name": "Lê Văn C",
        "captain_phone": "5647382910",
    },
    {
        "name": "Tàu D",
        "registration_number": "NA4567890",
        "address": "Cảng D",
        "status": "maintenance",
        "description": "Mô tả D",
        "speed": 25.0,
        "captain_name": "Phạm Quốc D",
        "captain_phone": "2938475610",
    },
    {
        "name": "Tàu E",
        "registration_number": "NA5678901",
        "address": "Cảng E",
        "status": "warning",
        "description": "Mô tả E",
        "speed": 40.0,
        "captain_name": "Vũ Thị E",
        "captain_phone": "1928374650",
    },
]

users_data = [
    {
        "username": "admin1",
        "password": "password123",
        "role": "admin",
        "is_active": True,
        "is_staff": True,
        "email": "admin1@example.com",
        "phone": "1234567890",
        "address": "123 Admin Street",
    },
    {
        "username": "thuyenvien1",
        "password": "1234",
        "role": "moderator",
        "is_active": True,
        "email": "moderator1@example.com",
        "phone": "0987654321",
        "address": "456 Moderator Lane",
    },
    {
        "username": "user1",
        "password": "password789",
        "role": "user",
        "is_active": True,
        "email": "user1@example.com",
        "phone": "1122334455",
        "address": "789 User Avenue",
    },
    {
        "username": "admin2",
        "password": "adminpassword",
        "role": "admin",
        "is_active": True,
        "email": "admin2@example.com",
        "phone": "2233445566",
        "address": "321 Admin Boulevard",
    },
    {
        "username": "moderator2",
        "password": "password1234",
        "role": "moderator",
        "is_active": False,
        "email": "moderator2@example.com",
        "phone": "6677889900",
        "address": "654 Moderator Court",
    },
    {
        "username": "haidoi2",
        "password": "1234",
        "role": "admin",
        "is_active": True,
        "is_superuser": True,
        "is_staff": True,
        "email": "haidoi2@example.com",
        "phone": "3344556677",
        "address": "987 Superuser Way",
    },
]
