SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS favorites;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS users;

SET FOREIGN_KEY_CHECKS = 1;

-- 用户表
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    nickname VARCHAR(50) NOT NULL,
    location VARCHAR(100)
);

-- 商品表
CREATE TABLE items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    trade_location VARCHAR(100),
    status VARCHAR(20) DEFAULT 'available',  -- available（在售）、reserved（已预订）、completed（已成交）
    poster_id INT NOT NULL,
    FOREIGN KEY (poster_id) REFERENCES users(user_id)
);

-- 评论表
CREATE TABLE comments (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT NOT NULL,
    commenter_id INT NOT NULL,
    content TEXT NOT NULL,
    comment_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (commenter_id) REFERENCES users(user_id)
);

-- 点赞表
CREATE TABLE likes (
    like_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT NOT NULL,
    liker_id INT NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (liker_id) REFERENCES users(user_id),
    UNIQUE (item_id, liker_id)  -- 防止同一用户重复点赞同一商品
);

-- 收藏表
CREATE TABLE favorites (
    favorite_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items(item_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE (item_id, user_id)  -- 防止同一用户重复收藏同一商品
);
