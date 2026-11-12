"""Calculate sale prices after a percentage discount."""


def discounted_prices(prices, discount_rate):
    output = []
    for price in prices:
        adjusted = price * (1 - discount_rate)
        output.append(round(adjusted, 2))
    return output


def main():
    products = [100.0, 50.0, 30.0]
    discount = 0.10
    print("Sale prices:", discounted_prices(products, discount))


if __name__ == "__main__":
    main()
