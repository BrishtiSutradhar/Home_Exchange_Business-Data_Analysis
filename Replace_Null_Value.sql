
--Replace Null Value From Subscription table
SELECT
  subscription_date,
  user_id,
  renew,
  first_subscription_date,
  first_subscription,
  referral,
  payment3x,
  payment2,
  payment3,
  IFNULL(country,'unknown') AS country,
  IFNULL(region, 'unknown') AS region,
  IFNULL(city,'unknown') AS city,
  IFNULL(department,'unknown') AS department,
  IFNULL(codeCountry,'unknown')AS codeCountry,
  IFNULL(countryName,'unknown')AS countryName,
FROM
`home_exchange.subscriptions_2`
ORDER BY
  user_id DESC
