from collections import defaultdict

class DuplicateAccountsDetector:
    def accounts_merge(self, accounts):
        """
        This function merges the duplicate accounts based on whether or not
        they share the same email. It also creates a list of the accounts
        that need to be removed from our original list of accounts.
        :param accounts: A list of lists representing the accounts. Each
        nested list is an account with the name on the account and the emails
        linked to it.
        :return: A tuple with each value as an element. The first element is
        the list of accounts merged but without the removal of the duplicate
        accounts. The second element is a list of indices of the accounts that
        need to be removed.
        """

        # In the section below, we are mapping the emails to the id, which
        # in our case is the index of the account in the list of accounts
        emails_to_id_mapping = defaultdict(set)  # key = email, value = id
        keys_list = list(accounts)
        for index, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                emails_to_id_mapping[email].add(index)

        # In the section below, we are checking the dictionary we created
        # to see which key (email in our case) has multiple items mapped to it
        # and appending the items of that key to a list which will be used
        # later to allow us to delete these accounts
        accounts_linked = []
        for i, account in enumerate(emails_to_id_mapping):
            accounts_using_email = emails_to_id_mapping[account]
            if len(accounts_using_email) > 1:
                accounts_linked.append(accounts_using_email)

        # In the section below, we create a list of indices of the accounts
        # that need to be deleted since they are duplicates.
        # We loop through and merge the duplicate accounts
        # We will always delete the second duplicate account found and not
        # the first. This could be changed according to your application.
        # Note: The merged accounts will have the email they shared listed
        # twice on the account. That still requires a few lines of code to
        # handle deleting it.
        accounts_to_delete_index = []
        for i in accounts_linked:
            list_linked_accounts = list(i)
            counter = 0
            for j in list_linked_accounts:
                accounts[list_linked_accounts[counter]] = accounts[list_linked_accounts[counter]] + accounts[list_linked_accounts[counter+1]][1:]
                accounts_to_delete_index.append(list_linked_accounts[counter+1])
                list_linked_accounts.pop(counter+1)
                counter +=1

        # we return the list of accounts along with the indices of the
        # accounts that need to be deleted.
        # The deletion/removal of the duplicate account is handled by
        # our class function delete_duplicate_accounts()
        return accounts, accounts_to_delete_index


    def delete_duplicate_accounts(self, accounts):
        """
        This function removes the duplicate accounts from the passed in list
        of accounts
        :param accounts: A list of lists that includes the accounts
        :return: A list of the accounts with the duplicate accounts removed.
        Note: The emails shared by two or more users were added to the first
        account found using that email. That still needs to be taken care of.
        """
        
        accounts_to_delete = self.accounts_merge(accounts)[1]
        accounts = [i for j, i in enumerate(accounts) if j not in accounts_to_delete]
        return accounts


if __name__ == '__main__':
    # Test Case
    accounts_to_merge = [["Daniel","danielsmith@mail.com","john_newyork@mail.com"],["Daniel","danielsmith@mail.com","dan00@mail.com"],["Mary","mary@mail.com", "johnnybravo@mail.com"],["John","johnnybravo@mail.com"]]
    merge_accounts = DuplicateAccountsDetector()
    merged = merge_accounts.delete_duplicate_accounts(accounts_to_merge)
    print(merged)
