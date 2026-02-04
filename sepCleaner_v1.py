import os

def process_markdown_files(folder_path):
    """
    处理指定文件夹下所有markdown文件，删除指定标记及标记外的内容
    
    Args:
        folder_path: 存放markdown文件的文件夹路径
    """
    # 定义需要匹配的两个关键标记
    start_marker = "转至元数据起始"  # 删除此标记及之前的所有内容
    end_marker = "其他版本Wiki"      # 删除此标记及之后的所有内容
    
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 {folder_path} 不存在！")
        return
    
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 只处理markdown文件（.md后缀）
        if filename.lower().endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 找到起始标记的位置（标记结束的位置 = 标记起始位置 + 标记长度）
                start_idx = content.find(start_marker)
                if start_idx != -1:
                    start_idx += len(start_marker)  # 跳过"转至元数据起始"本身
                
                # 找到结束标记的起始位置（直接截断，不包含标记本身）
                end_idx = content.find(end_marker)
                
                # 检查标记是否存在且顺序正确
                if start_idx == -1:
                    print(f"警告：文件 {filename} 中未找到 '{start_marker}' 标记，跳过处理")
                    continue
                if end_idx == -1:
                    print(f"警告：文件 {filename} 中未找到 '{end_marker}' 标记，跳过处理")
                    continue
                if start_idx >= end_idx:
                    print(f"警告：文件 {filename} 中 '{start_marker}' 在 '{end_marker}' 之后，跳过处理")
                    continue
                
                # 截取两个标记之间的内容（不包含标记本身）
                new_content = content[start_idx : end_idx]
                
                # 写入处理后的内容（覆盖原文件）
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"成功处理文件：{filename}")
            
            except Exception as e:
                print(f"处理文件 {filename} 时出错：{str(e)}")

if __name__ == "__main__":
    # 指定目标文件夹路径（可根据实际情况修改）
    target_folder = "sitemap_v11wiki"
    # 执行处理函数
    process_markdown_files(target_folder)
    print("所有markdown文件处理完成！")