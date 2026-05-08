# Google Analytics Setup Guide

## Why Track Visits?

Google Analytics 4 (GA4) will let you track:
- **Total visits** to your blog
- **Individual post reads** (which projects are most popular)
- **Reading depth** (how far people scroll in each post)
- **Traffic sources** (where readers come from)
- **Geography** (which countries visit)
- **Devices** (desktop vs mobile)

**Privacy:** The implementation includes IP anonymization and respects user privacy.

---

## Step 1: Create Google Analytics Account

1. Go to **https://analytics.google.com/**
2. Click **"Start measuring"**
3. Create an account:
   - Account name: "Data Science Blog" (or your preference)
   - Click **Next**
4. Create a property:
   - Property name: "petr-salomoun.github.io"
   - Time zone: Your timezone
   - Currency: Your currency
   - Click **Next**
5. Business information:
   - Industry: "Science & Technology" or "Publishing"
   - Business size: "Small"
   - Click **Next**
6. Business objectives:
   - Select "Examine user behavior"
   - Click **Create**
7. Accept the Terms of Service

---

## Step 2: Set Up Data Stream

1. On the "Web stream details" page:
   - Website URL: `https://petr-salomoun.github.io`
   - Stream name: "Blog"
   - Click **Create stream**

2. You'll see your **Measurement ID** (looks like `G-XXXXXXXXXX`)
   - **COPY THIS ID** - you'll need it!

---

## Step 3: Add Analytics to Your Blog

1. Open `_config.yml` in your blog repository
2. Find the line:
   ```yaml
   # google_analytics: G-XXXXXXXXXX
   ```
3. Uncomment it and replace with your real ID:
   ```yaml
   google_analytics: G-1234567890
   ```
4. Save the file
5. Commit and push:
   ```bash
   git add _config.yml
   git commit -m "Enable Google Analytics tracking"
   git push origin main
   ```

---

## Step 4: Verify It's Working

1. Visit your blog: **https://petr-salomoun.github.io**
2. In Google Analytics, go to:
   - **Reports** → **Realtime**
3. You should see yourself as a current visitor!

If you don't see activity:
- Wait 1-2 minutes (GitHub Pages rebuild time)
- Clear your browser cache
- Try in an incognito window

---

## What You'll See in Analytics

### Homepage Dashboard

After 24-48 hours, you'll see:

**Realtime Overview:**
- Active users right now
- Pages being viewed
- Traffic sources

**Acquisition:**
- Where visitors come from (Google, direct, social media, etc.)

**Engagement:**
- Which posts are most read
- Average time on page
- Scroll depth (how far people read)

**Demographics:**
- Countries
- Cities
- Devices (desktop/mobile/tablet)

### Custom Events We Track

The implementation automatically tracks:

1. **Page Views** - Every page load
   ```
   Event: page_view
   Properties: page_title, page_url
   ```

2. **Post Reads** - When someone visits a blog post
   ```
   Event: post_read
   Category: engagement
   Label: [post title]
   ```

3. **Scroll Depth** - Reading progress
   ```
   Event: scroll_depth
   Values: 25%, 50%, 75%, 100%
   Label: [post title]
   ```

### Most Useful Reports

**To see which posts are popular:**
1. Go to **Reports** → **Engagement** → **Pages and screens**
2. You'll see a list of URLs with view counts
3. Posts are at `/posts/YYYY/MM/DD/title/`

**To see reading completion:**
1. Go to **Reports** → **Engagement** → **Events**
2. Look for the `scroll_depth` event
3. See how many readers reach 100% (finished the post)

**To see traffic sources:**
1. Go to **Reports** → **Acquisition** → **Traffic acquisition**
2. See if readers come from Google, social media, direct links, etc.

---

## Privacy Considerations

The tracking code includes:
- **IP anonymization** - Visitor IPs are masked
- **Cookie consent** - Uses SameSite=None;Secure flags
- **No PII** - No personal information collected

You should add a privacy policy mentioning analytics. Add to your About page:

```markdown
## Privacy

This blog uses Google Analytics to understand readership and improve content.
Analytics collects:
- Page views and time spent
- General location (country/city)
- Device type and browser
- Referral sources

Your IP address is anonymized. No personal data is collected or stored.
You can opt out using browser extensions or privacy settings.
```

---

## Advanced: Creating Custom Reports

### "Most Popular Posts" Report

1. Go to **Explore** → **Create new exploration**
2. Choose **Free form**
3. Dimensions: Page path and screen class, Page title
4. Metrics: Event count, Users
5. Drag Page title to Rows
6. Drag Event count to Values
7. Filter: Event name = "post_read"
8. Save as "Most Popular Posts"

### "Reading Completion Funnel"

1. Go to **Explore** → **Funnel exploration**
2. Steps:
   - Step 1: page_view
   - Step 2: scroll_depth (25%)
   - Step 3: scroll_depth (50%)
   - Step 4: scroll_depth (75%)
   - Step 5: scroll_depth (100%)
3. See what % of readers finish posts

---

## Troubleshooting

**"No data appearing"**
- Check that `google_analytics` is set in `_config.yml`
- Verify the ID starts with `G-` (not `UA-` - that's old Universal Analytics)
- Wait 24-48 hours for data to populate
- Check browser console for errors (F12 → Console)

**"Only seeing my own visits"**
- That's normal! You'll see real traffic once others visit
- Exclude your own IP in Admin → Data Streams → Configure tag settings

**"Events not showing up"**
- Events may take 24-48 hours to appear in standard reports
- Check **Realtime** → **Event count by Event name** for immediate feedback

---

## Cost

Google Analytics 4 is **completely free** with:
- Up to 10 million events per month
- Unlimited users
- Full feature set

Your blog will likely use < 100,000 events/month, well under the limit.

---

## Next Steps After Setup

1. **Check weekly** to see which posts are popular
2. **Use data** to decide what topics to explore next
3. **Monitor traffic sources** to know where to share new posts
4. **Track scroll depth** to see if posts are too long

---

## Summary

**To enable tracking:**
1. Create Google Analytics account (5 min)
2. Copy your Measurement ID
3. Add to `_config.yml`: `google_analytics: G-XXXXXXXXXX`
4. Push to GitHub
5. Done!

**What you get:**
- Real-time visitor count
- Post popularity rankings
- Reading completion rates
- Traffic source analysis
- Geographic data

**Privacy:**
- IP anonymization enabled
- No personal data collected
- GDPR/CCPA compliant

---

**File location:** The tracking code is in `_includes/google-analytics.html`  
**Configuration:** `_config.yml` → `google_analytics` setting  
**Documentation:** https://support.google.com/analytics/

Once enabled, you'll know exactly which projects resonate most with readers!
