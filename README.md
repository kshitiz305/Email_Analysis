# LinkedIn Automation Workflow for n8n

This project contains an n8n workflow that automatically posts to LinkedIn on a daily basis, promoting your agency's LinkedIn automation service.

## 🚀 Features

- **Daily Automated Posting**: Posts every day at a scheduled time
- **Dynamic Content Generation**: Creates varied posts using templates
- **Agency Promotion**: Focuses on promoting your LinkedIn automation service
- **Content Validation**: Ensures posts meet LinkedIn's character limits
- **Success/Error Logging**: Tracks all posting activities
- **Hashtag Optimization**: Includes relevant hashtags for better reach

## 📋 Prerequisites

1. **n8n Installation**: You need n8n installed and running
2. **LinkedIn Developer Account**: Access to LinkedIn's API
3. **LinkedIn App Credentials**: Client ID and Client Secret

## 🔧 Setup Instructions

### 1. Install n8n

If you haven't installed n8n yet:

```bash
# Using npm
npm install n8n -g

# Using Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

### 2. LinkedIn API Setup

1. Go to [LinkedIn Developers](https://www.linkedin.com/developers/)
2. Create a new app
3. Get your **Client ID** and **Client Secret**
4. Add the following OAuth 2.0 redirect URLs:
   - `http://localhost:5678/callback`
   - `https://your-n8n-domain.com/callback` (if using hosted n8n)

### 3. Import the Workflow

1. Open your n8n instance (usually at `http://localhost:5678`)
2. Click on "Workflows" in the sidebar
3. Click "Import from file"
4. Select the `linkedin-automation-workflow.json` file
5. The workflow will be imported with all nodes configured

### 4. Configure LinkedIn Credentials

1. In the imported workflow, click on the "Post to LinkedIn" node
2. Click on "Add Credential" next to the LinkedIn field
3. Select "LinkedIn OAuth2 API"
4. Enter your LinkedIn app credentials:
   - **Client ID**: Your LinkedIn app client ID
   - **Client Secret**: Your LinkedIn app client secret
5. Click "Save" and authorize the connection

### 5. Customize the Schedule

The workflow is set to post daily. To modify the schedule:

1. Click on the "Daily Trigger" node
2. Modify the cron expression:
   - **Daily at 9 AM**: `0 9 * * *`
   - **Every Monday at 10 AM**: `0 10 * * 1`
   - **Every 6 hours**: `0 */6 * * *`

### 6. Customize Content Templates

To modify the post content:

1. Click on the "Generate Post Content" node
2. Edit the `postTemplates` array in the JavaScript code
3. Add your own templates or modify existing ones
4. Update hashtags in the `additionalHashtags` array

## 📝 Workflow Structure

```
Daily Trigger → Generate Post Content → Validate Post Length → Post to LinkedIn → Log Success
                                    ↓
                                Log Error (if content too long)
```

### Node Descriptions:

1. **Daily Trigger**: Cron job that runs the workflow daily
2. **Generate Post Content**: Creates dynamic post content using templates
3. **Validate Post Length**: Ensures posts don't exceed LinkedIn's 1300 character limit
4. **Post to LinkedIn**: Publishes the content to LinkedIn
5. **Log Success/Error**: Records the results of each posting attempt

## 🎯 Content Strategy

The workflow includes 8 different post templates that:

- Promote your agency's LinkedIn automation service
- Use engaging emojis and hashtags
- Include dynamic day counting
- Maintain professional tone while being engaging
- Focus on business benefits and innovation

## 🔒 Security Considerations

- Store LinkedIn credentials securely in n8n
- Use environment variables for sensitive data
- Regularly rotate API keys
- Monitor workflow execution logs

## 📊 Monitoring

The workflow includes built-in logging that tracks:
- Successful posts with timestamps
- Post content and length
- Error messages for failed attempts
- Template usage statistics

## 🚨 Troubleshooting

### Common Issues:

1. **Authentication Errors**: Ensure LinkedIn credentials are properly configured
2. **Content Too Long**: Check the character limit validation
3. **Rate Limiting**: LinkedIn has posting limits; monitor for rate limit errors
4. **Network Issues**: Ensure stable internet connection for API calls

### Debug Steps:

1. Check n8n execution logs
2. Verify LinkedIn app permissions
3. Test the workflow manually first
4. Monitor LinkedIn API status

## 📈 Optimization Tips

1. **A/B Testing**: Create multiple workflows with different content strategies
2. **Timing Optimization**: Test different posting times for better engagement
3. **Content Variety**: Regularly update templates to avoid repetition
4. **Analytics Integration**: Add webhook nodes to track post performance

## 🔄 Maintenance

- Review and update content templates monthly
- Monitor LinkedIn API changes
- Update hashtags based on trending topics
- Backup workflow configurations regularly

## 📞 Support

For issues with:
- **n8n**: Check [n8n documentation](https://docs.n8n.io/)
- **LinkedIn API**: Refer to [LinkedIn API docs](https://developer.linkedin.com/)
- **Workflow Logic**: Review the JavaScript code in each node

## 📄 License

This workflow is provided as-is for educational and business purposes. Ensure compliance with LinkedIn's terms of service and your local regulations.