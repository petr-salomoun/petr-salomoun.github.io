# Debugging Google Analytics

## Quick Check: Is Analytics Loading?

### Method 1: Browser Console

1. Open your blog post: https://petr-salomoun.github.io/posts/2026/05/08/tri-pollution-health-effect/
2. Press **F12** (or Ctrl+Shift+I) to open Developer Tools
3. Go to the **Console** tab
4. Type: `dataLayer`
5. Press Enter

**✅ Working:** You'll see an array with tracking events  
**❌ Not working:** You'll see `undefined`

### Method 2: Network Tab

1. Open Developer Tools (F12)
2. Go to the **Network** tab
3. Reload the page
4. Filter by: `gtag` or `google-analytics`
5. Look for requests to `www.googletagmanager.com`

**✅ Working:** You'll see multiple requests (gtag/js loading, events being sent)  
**❌ Not working:** No requests appear

### Method 3: View Page Source

1. Right-click the page → **View Page Source**
2. Search for: `gtag` (Ctrl+F)

**✅ Working:** You'll see the Google Analytics script with your ID `G-75QV6XS4MX`  
**❌ Not working:** No gtag script found

---

## What Should Appear

### On Homepage (/)

**Events sent:**
```javascript
page_view {
  page_title: "Home",
  page_path: "/"
}
```

### On Blog Posts (e.g., /posts/2026/05/08/tri-pollution-health-effect/)

**Events sent:**
```javascript
page_view {
  page_title: "Industrial Pollution and Public Health...",
  page_path: "/posts/2026/05/08/tri-pollution-health-effect/"
}

post_read {
  event_category: "engagement",
  event_label: "Industrial Pollution and Public Health..."
}

scroll_depth {  // Sent at 25%, 50%, 75%, 100% scroll
  event_category: "engagement",
  event_label: "Industrial Pollution and Public Health...",
  value: 25  // or 50, 75, 100
}
```

---

## Verification in Google Analytics

### Real-Time Check

1. Go to **Google Analytics** → https://analytics.google.com/
2. Select your property: `petr-salomoun.github.io`
3. Go to **Reports** → **Realtime**
4. Open your blog in another tab
5. You should immediately see:
   - **Users:** 1 active user
   - **Page views:** Your current page
   - **Event count:** Events being tracked

### Check Custom Events

1. In Realtime → **Event count by Event name**
2. You should see:
   - `page_view`
   - `post_read` (when viewing a post)
   - `scroll_depth` (when scrolling)

If you DON'T see these events, the analytics aren't loading.

---

## Common Issues & Fixes

### Issue 1: "Google Analytics ID not found in page source"

**Diagnosis:** Analytics code not being included

**Fix:**
1. Check `_config.yml` has:
   ```yaml
   google_analytics: G-75QV6XS4MX
   ```
2. Verify `_includes/head-custom.html` exists and contains:
   ```liquid
   {% include google-analytics.html %}
   ```
3. Rebuild the site: `git push origin main`

### Issue 2: "gtag script loads but events don't fire"

**Diagnosis:** JavaScript error in analytics code

**Fix:**
1. Open Console (F12)
2. Look for red error messages
3. Check if `gtag` function is defined: type `gtag` in console
4. If undefined, the script didn't load properly

### Issue 3: "Only page_view events, no post_read or scroll_depth"

**Diagnosis:** Post-specific code not executing

**Possible causes:**
- Post layout isn't `post` (check frontmatter)
- JavaScript error preventing execution
- Browser blocking the code

**Fix:**
1. Check post frontmatter has `layout: post`
2. Look for errors in Console
3. Try in an incognito window (no ad blockers)

### Issue 4: "Events work locally but not on GitHub Pages"

**Diagnosis:** GitHub Pages caching or build issue

**Fix:**
1. Force rebuild: make a trivial change, commit, push
2. Clear GitHub Pages cache: wait 5-10 minutes
3. Hard refresh browser: Ctrl+Shift+R

---

## Manual Test

### Test the Full Flow

1. **Visit homepage** → Check Realtime for `page_view`
2. **Click a blog post** → Check for `page_view` + `post_read`
3. **Scroll to 30%** → Check for `scroll_depth` value=25
4. **Scroll to 60%** → Check for `scroll_depth` value=50
5. **Scroll to bottom** → Check for `scroll_depth` value=100

All events should appear in **Realtime** → **Event count by Event name** within seconds.

---

## Expected Analytics Flow

```
User visits homepage
  └─> page_view event sent
  
User clicks post
  └─> page_view event sent
  └─> post_read event sent (because layout=post)
  
User scrolls past 25% of page
  └─> scroll_depth event sent (value=25)
  
User scrolls past 50%
  └─> scroll_depth event sent (value=50)
  
etc.
```

---

## Checking Event Data

### In Google Analytics (after 24-48 hours)

1. **Reports** → **Engagement** → **Events**
2. Look for these custom events:
   - `post_read` → Shows how many posts were viewed
   - `scroll_depth` → Shows reading completion rates

3. **Reports** → **Engagement** → **Pages and screens**
   - See page views per post
   - Compare which posts get most traffic

---

## Privacy Note

The tracking respects privacy:
- `anonymize_ip: true` → Visitor IPs are masked
- No personal data collected
- Cookies use `SameSite=None;Secure` flags
- GDPR/CCPA compliant

---

## Current Status

**GA ID configured:** `G-75QV6XS4MX` ✅  
**Analytics include:** `_includes/google-analytics.html` ✅  
**Head custom:** `_includes/head-custom.html` ✅ (FIXED)  
**Theme support:** Cayman includes `head-custom.html` ✅

**Should now work after the latest push (commit bd606f3)**

---

## If Still Not Working

Try this diagnostic script in Console:

```javascript
// Check if gtag is loaded
console.log('gtag defined?', typeof gtag !== 'undefined');

// Check if dataLayer exists
console.log('dataLayer exists?', typeof dataLayer !== 'undefined');

// Check config
if (typeof dataLayer !== 'undefined') {
  console.log('dataLayer contents:', dataLayer);
}

// Manually fire a test event
if (typeof gtag !== 'undefined') {
  gtag('event', 'test_event', {
    'event_category': 'debug',
    'event_label': 'manual_test'
  });
  console.log('Test event fired - check Realtime in GA');
}
```

If `gtag` is undefined, analytics aren't loading.  
If `gtag` is defined, try the manual event and check Realtime.

---

**File location:** `_includes/google-analytics.html`  
**Configuration:** `_config.yml` → `google_analytics: G-75QV6XS4MX`  
**Latest fix:** commit bd606f3 (removed duplicate head tags)

Wait 1-2 minutes for GitHub Pages to rebuild, then test!
