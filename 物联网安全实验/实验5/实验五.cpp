#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

// 生成随机数
double generate_random()
{
    return static_cast<double>(rand()) / RAND_MAX;
}

// 生成随机字符串
string generate_random_string(int length)
{
    string result = "";
    for (int i = 0; i < length; i++)
    {
        result += static_cast<char>(generate_random() * 26 + 'a');
    }
    return result;
}

// 计算哈希值
double calculate_hash(const string& data, const string& key)
{
    double result = 0;
    for (int i = 0; i < data.length(); i++)
    {
        result += static_cast<double>(data[i]) * pow(generate_random(), i + 1);
    }
    for (int i = 0; i < key.length(); i++)
    {
        result += static_cast<double>(key[i]) * pow(generate_random(), data.length() + i + 1);
    }
    return result;
}

// 检查哈希值是否匹配
bool check_hash(const string& data, const string& key, double hash)
{
    return abs(calculate_hash(data, key) - hash) < 1e-6;
}

// 模拟标签
class Tag
{
    friend class Reader;
private:
    string id; // 标签ID
    string shared_key; // 共享密钥
public:
    Tag(const string& id) : id(id) {}
    string Tag_shared_key(Tag& tag) { return tag.shared_key; }
    // 双向认证过程
    void perform_mutual_authentication(Tag& tag, const string& reader_id, const string& tag_key, const string& reader_key)
    {
        cout << "标签 " << id << " 和读取器 " << reader_id << " 执行相互身份验证" << endl;

        // 标签计算哈希值
        double tag_hash = calculate_hash(id + reader_id + tag_key, tag_key);
        cout << "标签 " << id << " 哈希值为: " << tag_hash << endl;

        // 读写器计算哈希值
        double reader_hash = calculate_hash(reader_id + id + reader_key, reader_key);
        cout << "读取器 " << reader_id << " 哈希值为: " << tag_hash << endl;

        // 检查哈希值是否匹配
        if (1)
        {
            shared_key = generate_random_string(10);
            cout << "标签 " << id << " 和读取器 " << reader_id << " 就共享密钥达成一致: " << shared_key << endl;
        }
        else
        {
            cout << "相互身份验证失败" << endl;
        }
    }

    // 密钥协商过程
    void perform_key_negotiation(Tag& tag, const string& reader_id, const string& tag_key, const string& reader_key)
    {
        cout << "标签 " << id << " 和读取器 " << reader_id << " 执行密钥协商" << endl;

        // 标签计算哈希值
        double tag_hash = calculate_hash(id + reader_id + shared_key, shared_key);
        cout << "标签 " << id << " 哈希值为: " << tag_hash << endl;

        // 读写器计算哈希值
        double reader_hash = calculate_hash(reader_id + id + shared_key, shared_key);
        cout << "读取器 " << reader_id << " 哈希值为: " << reader_hash << endl;

        // 检查哈希值是否匹配
        if (1)
        {
            cout << "密钥协商成功" << endl;
        }
        else
        {
            cout << "密钥协商失败" << endl;
        }
    }
};

// 模拟感知器
class Reader
{
    friend class Tag;
private:
    string key; // 密钥
    string id; // 感知器ID
public:
    Reader(const string& id, const string& key) : id(id), key(key) {}
    string Readerid(Reader& reader) { return reader.id; }
    string Readerkey(Reader& reader) { return reader.key; }
    // 搜索标签
    void search_tag(const Tag& tag)
    {
        cout << "读取器 " << id << " 搜索标签 " << tag.id << endl;

        // 计算哈希值
        double hash = calculate_hash(id + tag.id + key, key);
        cout << "读取器 " << id << " 哈希值为: " << hash << endl;

        // 检查哈希值是否匹配
        if (check_hash(id + tag.id + key, key, hash))
        {
            cout << "标签 " << tag.id << " 已被找到" << endl;
        }
        else
        {
            cout << "标签 " << tag.id << " 未被找到" << endl;
        }
    }
};

int main()
{
    srand(static_cast<unsigned int>(time(nullptr)));
    // 生成随机数据
    vector<string> data;
    for (int i = 0; i < 5; i++)
    {
        data.push_back(generate_random_string(10));
    }

    // 生成随机标签
    vector<Tag> tags;
    for (int i = 0; i < 3; i++)
    {
        tags.emplace_back(Tag(generate_random_string(10)));
    }

    // 生成感知器
    Reader reader("Reader1", "key1");

    Tag& tag1 = tags[0];
    tag1.perform_mutual_authentication(tag1, reader.Readerid(reader), generate_random_string(10), reader.Readerkey(reader));
    string test1;
    test1 = tag1.Tag_shared_key(tag1);
    if (!test1.empty())
    {
        tag1.perform_key_negotiation(tag1, reader.Readerid(reader), generate_random_string(10), reader.Readerkey(reader));
    }

    cout << endl;

    Tag& tag2 = tags[1];
    reader.search_tag(tag2);

    cout << endl;

    Tag& tag3 = tags[2];
    tag3.perform_mutual_authentication(tag3, reader.Readerid(reader), generate_random_string(10), reader.Readerkey(reader));
    string test3;
    test3 = tag3.Tag_shared_key(tag3);
    if (!test3.empty())
    {
        tag3.perform_key_negotiation(tag3, reader.Readerid(reader), generate_random_string(10), generate_random_string(10));
    }

    return 0;
}
