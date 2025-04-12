import sqlite3
# 创建SQLite数据库连接
conn = sqlite3.connect(':memory:')  # 使用内存数据库，测试用
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")
# 创建表结构（根据schema.sql调整）
def create_tables():
    cursor.executescript("""
    DROP TABLE IF EXISTS favorites;
    DROP TABLE IF EXISTS likes;
    DROP TABLE IF EXISTS comments;
    DROP TABLE IF EXISTS items;
    DROP TABLE IF EXISTS users;
    -- 用户表
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nickname TEXT NOT NULL,
        location TEXT
    );
    
    -- 商品表
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        trade_location TEXT,
        status TEXT DEFAULT 'available',
        poster_id INTEGER NOT NULL,
        FOREIGN KEY (poster_id) REFERENCES users(user_id)
    );
    
    -- 评论表
    CREATE TABLE comments (
        comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        commenter_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        comment_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (item_id) REFERENCES items(item_id),
        FOREIGN KEY (commenter_id) REFERENCES users(user_id)
    );
    
    -- 点赞表
    CREATE TABLE likes (
        like_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        liker_id INTEGER NOT NULL,
        FOREIGN KEY (item_id) REFERENCES items(item_id),
        FOREIGN KEY (liker_id) REFERENCES users(user_id),
        UNIQUE (item_id, liker_id)
    );
    
    -- 收藏表
    CREATE TABLE favorites (
        favorite_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (item_id) REFERENCES items(item_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        UNIQUE (item_id, user_id)
    );
""")
def insert_data():
    cursor.executescript("""
-- 用户数据
INSERT INTO users (nickname, location) VALUES
('小明', '北京市 海淀区'),
('小红', '上海市 徐汇区'),
('阿强', '广州市 天河区');

-- 商品数据
INSERT INTO items (name, description, price, trade_location, status, poster_id) VALUES
('二手iPhone 13', '95新，无划痕，128GB，支持面交', 3600.00, '中关村地铁站', 'available', 1),
('书桌', '实木书桌，长120cm，带抽屉', 280.00, '徐家汇地铁站', 'reserved', 2),
('山地自行车', '9成新，适合上班通勤', 980.00, '天河城广场', 'completed', 3);

-- 评论数据
INSERT INTO comments (item_id, commenter_id, content) VALUES
(1, 2, '还能便宜点吗？'),
(1, 3, '有发票吗？'),
(2, 1, '请问尺寸是多少？');

-- 点赞数据
INSERT INTO likes (item_id, liker_id) VALUES
(1, 2),
(2, 3),
(3, 1);

-- 收藏数据
INSERT INTO favorites (item_id, user_id) VALUES
(1, 3),
(2, 1),
(2, 3);

""")

query_all_items ="""
    -- 列出所有商品的核心信息
    SELECT 
    item_id AS 商品ID,
    name AS 商品名称,
    price AS 价格,
    status AS 状态,
    trade_location AS 交易地点
    FROM items
    ORDER BY item_id ASC; -- 按商品ID升序排列
"""
query_all_users = """
-- 列出所有用户的核心信息
SELECT 
    user_id AS 用户ID,
    nickname AS 昵称,
    location AS 住址
FROM users
ORDER BY user_id ASC;
"""
# 固定宽度版（更简单但适应性稍差）
def print_query_result(description, query, cursor):
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"\n=== {description} ===")
    for row in results:
        print(f"ID: {row[0]:<3} | 名称: {row[1]:<12} | 价格: {row[2]:<7} | 状态: {row[3]:<10} | 地点: {row[4]}")
# 执行测试
create_tables()
insert_data()
#test_queries()
print_query_result("列出所有的商品",query_all_items,cursor)
print_query_result("列出所有的用户",query_all_users,cursor)


# 关闭连接
conn.close()