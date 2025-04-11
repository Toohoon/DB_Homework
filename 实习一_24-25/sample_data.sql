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
