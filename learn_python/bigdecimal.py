from decimal import Decimal

# PyCharm按cmd+j然后输入main自动生成 if __name__ == ...
if __name__ == '__main__':
    """
    Decimal的构造方法只能用字符串或整数
    Rust的文档中提到，如果用f32或f64构造Decimal照样会出现精度丢失，因为float是primitive type无法获取浮点在哪一位digit上    
    """
    # float_compute_result: float = 2.07 - 2.07 * 8
    # 错误示例：Decimal构造方法入参中使用了float
    decimal_float_constructor_compute_result: Decimal = Decimal(2.07) - Decimal(2.07) * Decimal(8)
    decimal_str_constructor_compute_result: Decimal = Decimal('2.07') - Decimal('2.07') * Decimal(8)
    assert decimal_str_constructor_compute_result != decimal_float_constructor_compute_result
